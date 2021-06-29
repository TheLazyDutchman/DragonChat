import ClientConnection
from imutils.video import VideoStream
import socket
import window
from Chat.chatHandler import chatHandler
from Groups.groupHandler import groupHandler
from Creatures.creatureHandler import creatureHandler
from ServerHandler.EventHandler import EventHandler


serverIp = "212.187.9.198"

imgSendPort = 5555
imgRecvPort = 5556
textSendPort = 5557
textRecvPort = 5558
soundSendPort = 5559
soundRecvPort = 5560

userName = "testUser"

camera = VideoStream().start()

with ClientConnection.Connections(socket.gethostname(), "group", serverIp) as server:
    server.initialize_text_data(textSendPort, textRecvPort)

    group = groupHandler(userName, server.textSender)
    status, groupName = group.createGroup("group", '')

    creatures = creatureHandler(groupName, userName, server.textSender)

    chat = chatHandler(groupName, userName, server.textSender)

    handlers = {
        "group" : group,
        "creatures" : creatures,
        "chat" : chat
    }

    main = window.main(socket.gethostname(), "D&D messaging", server, handlers)

    eventListener = EventHandler(groupName, userName, server.textSender)
    eventListener.addListener("Message", main.handleMsg)
    eventListener.addListener("Initiative", main.handleInitiative)

    server.start_textLoop(eventListener.HandleEvent)

    main.start()