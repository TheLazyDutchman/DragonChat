import ClientConnection
from imutils.video import VideoStream
import socket
import window
from Chat.chatHandler import chatHandler
from Groups.groupHandler import groupHandler
from Creatures.CreatureHandler import CreatureHandler
from ServerHandler.EventHandler import EventHandler
from Initiative.InitiativeHandler import InitiativeHandler


serverIp = "212.187.9.198"

imgSendPort = 5555
imgRecvPort = 5556
textSendPort = 5557
textRecvPort = 5558
soundSendPort = 5559
soundRecvPort = 5560

userName = "testUser"

camera = VideoStream().start()

with ClientConnection.Connections(userName, "group", serverIp) as server:
    server.initialize_text_data(textSendPort, textRecvPort)

    group = groupHandler(userName, server.textSender)
    status, groupName = group.createGroup("group", '')

    creatures = CreatureHandler(groupName, userName, server.textSender)

    chat = chatHandler(groupName, userName, server.textSender)

    initiative = InitiativeHandler(groupName, userName, server.textSender)

    handlers = {
        "group" : group,
        "creatures" : creatures,
        "chat" : chat,
        "initiative" : initiative
    }

    main = window.main(socket.gethostname(), "D&D messaging", server, handlers)

    eventListener = EventHandler(groupName, userName, server.textSender)
    eventListener.addListener("Message", main.handleMsg)
    eventListener.addListener("Initiative", main.initiativeWindow.handleInitiativeUpdate)
    eventListener.addListener("Start turn", main.initiativeWindow.handleStartTurn)
    eventListener.addListener("Creatures", main.creaturesWindow.handleServerCreatures)

    server.start_textLoop(eventListener.HandleEvent)

    main.start()