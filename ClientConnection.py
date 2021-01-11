import imagezmq
import zmq
import threading
import traceback
from cv2 import cv2
from VideoStreamSubscriber import VideoStreamSubscriber
import numpy as np
import pyaudio

class Connections:

    def __init__(self, name, serverIp):
        self.name = name
        self.serverIp = serverIp
        self.imgStarted = False

    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.disconnect()

    def start_imageLoop(self, imgSendPort, imgRecvPort, camera):
        try:
            self.imageSender = imagezmq.ImageSender(connect_to=f"tcp://{self.serverIp}:{imgSendPort}")
            self.imageReciever = VideoStreamSubscriber(self.serverIp, imgRecvPort)
        except Exception:
            print("unhandled exception")
            traceback.print_exc()

        self.camera = camera

        self.images = {}

        imgThread = threading.Thread(target=self.imageLoop)
        imgThread.daemon = True
        imgThread.start()

        self.imgStarted = True

    def start_textLoop(self, textSendPort, textRecvPort, textCallBack):
        context = zmq.Context()
        self.textSender = context.socket(zmq.REQ)
        self.textSender.connect(f"tcp://{self.serverIp}:{textSendPort}")
        self.textReciever = context.socket(zmq.SUB)
        self.textReciever.connect(f"tcp://{self.serverIp}:{textRecvPort}")
        self.textReciever.subscribe("")
        self.textCallBack = textCallBack
        
        txtThread = threading.Thread(target=self.textLoop)
        txtThread.daemon = True
        txtThread.start()

    def start_soundLoop(self, soundSendPort, soundRecvPort):
        context = zmq.Context()
        self.soundSender = context.socket(zmq.REQ)
        self.soundSender.connect(f"tcp://{self.serverIp}:{soundSendPort}")
        self.soundReciever = context.socket(zmq.SUB)
        self.soundReciever.connect(f"tct://{self.serverIp}:{soundRecvPort}")
        self.soundReciever.subscribe("")
        self.audio = pyaudio.PyAudio()

        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 2
        self.fs = 44100  # Record at 44100 samples per second

        soundThread = threading.Thread(target=self.soundLoop)
        soundThread.daemon = True
        soundThread.start()


    def imageLoop(self):
        try:
            while True:
                image = self.camera.read()
                _, sendImg = cv2.imencode(".jpg", image)
                self.imageSender.send_jpg(self.name, sendImg)

                # recv images from the server
                self.images = self.imageReciever.receive()
            
            

        except (KeyboardInterrupt, SystemExit):
            print("image loop interrupted by keyboard")
        except Exception:
            print("unhandled exception")
            traceback.print_exc()

    def recv_images(self):
        images = {}
        items = self.images.items()
        for name, image in items:
            images[name] = cv2.imdecode(np.frombuffer(image, dtype='uint8'), cv2.IMREAD_COLOR)
        return images

    def textLoop(self):
        try:
            lastText = ""
            while True:
                data = self.textReciever.recv_pyobj()
                if not data is lastText and len(data[1]) > 0:
                    lastText = data
                    self.textCallBack(data)

        except (KeyboardInterrupt, SystemExit):
            print("text loop interrupted by keyboard")
        except Exception:
            print("unhandled exception")
            traceback.print_exc()

    def send_msg(self, msg):
        self.textSender.send_pyobj(msg)

        self.textSender.recv()

    def soundLoop(self):
        try:
            recordStream = self.audio.open(rate=self.fs, 
                                            channels=self.channels, 
                                            format=self.sample_format,
                                            input=True)

            # we open a separate stream for every client other than ourselves
            clients = dict()

            while True:
                sound = recordStream.read(self.chunk)
                self.soundSender.send_pyobj((self.name, sound))

                # recv sound from the server
                name, sound = self.soundReciever.recv_pyobj()
                if not name == self.name:
                    if not name in clients:
                        clients[name] = self.audio.open(rate=self.fs, 
                                                        channels=self.channels, 
                                                        format=self.sample_format,
                                                        output=True)
                    
                    clients[name].write(sound)
            
            

        except (KeyboardInterrupt, SystemExit):
            print("image loop interrupted by keyboard")
        except Exception:
            print("unhandled exception")
            traceback.print_exc()

    def disconnect(self):
        if self.imgStarted:
            self.imageSender.close()
            self.imageReciever.close()