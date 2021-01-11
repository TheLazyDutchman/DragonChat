import imagezmq
import zmq
import threading
import traceback


imgRecvPort = 5555
imgSendPort = 5556
imageHub = imagezmq.ImageHub(open_port=f"tcp://*:{imgRecvPort}")
imageSender = imagezmq.ImageSender(connect_to=f"tcp://*:{imgSendPort}", REQ_REP=False)

Context = zmq.Context()

txtRecvPort = 5557
txtSendPort = 5558
textRecv = Context.socket(zmq.REP)
textRecv.bind(f"tcp://*:{txtRecvPort}")
textSend = Context.socket(zmq.PUB)
textSend.bind(f"tcp://*:{txtSendPort}")

soundRecvPort = 5559
soundSendPort = 5560
soundRecv = Context.socket(zmq.REP)
soundRecv.bind(f"tcp://*:{soundRecvPort}")
soundSend = Context.socket(zmq.PUB)
soundSend.bind(f"tcp://*:{soundSendPort}")

def start_image():
    try:
        while True:
            data, image = imageHub.recv_jpg()
            imageSender.send_jpg(data, image)
            imageHub.send_reply(b'OK')

    except (KeyboardInterrupt, SystemExit):
        print("image loop interrupted by keyboard")
    except Exception:
        print("unhandled exception")
        traceback.print_exc()
    finally:
        imageHub.close()
        imageSender.close()

def start_text():
    try:
        while True:
            data = textRecv.recv_pyobj()
            textSend.send_pyobj(data)
            # send reply
            textRecv.send(b'OK')

    except (KeyboardInterrupt, SystemExit):
        print("text loop interrupted by keyboard")
    except Exception:
        print("unhandled exception")
        traceback.print_exc()
    finally:
        textRecv.close()
        textSend.close()

def start_sound():
    try:
        while True:
            data = soundRecv.recv_pyobj()
            soundSend.send_pyobj(data)
            # send reply
            soundRecv.send(b'OK')

    except (KeyboardInterrupt, SystemExit):
        print("sound loop interrupted by keyboard")
    except Exception:
        print("unhandled exception")
        traceback.print_exc()
    finally:
        soundRecv.close()
        soundSend.close()


if __name__ == '__main__':
    imgThread = threading.Thread(target=start_image)
    imgThread.start()
    txtThread = threading.Thread(target=start_text)
    txtThread.start()
    soundThread = threading.Thread(target=start_sound)
    soundThread.start()