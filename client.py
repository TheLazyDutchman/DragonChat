import ClientConnection
from imutils.video import VideoStream
import time
import socket
import window


serverIp = "212.187.9.198"
serverIp = "127.0.0.1"
imgSendPort = 5555
imgRecvPort = 5556
textSendPort = 5557
textRecvPort = 5558
soundSendPort = 5559
soundRecvPort = 5560

camera = VideoStream().start()

with ClientConnection.Connections(socket.gethostname(), serverIp) as server:
    main = window.main(socket.gethostname(), "D&D messaging", server, server.send_msg)

    server.start_imageLoop(imgSendPort, imgRecvPort, camera)
    server.start_textLoop(textSendPort, textRecvPort, main.handleMsg)
    # server.start_soundLoop(soundSendPort, soundRecvPort)


    main.start()