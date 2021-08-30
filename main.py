import ClientConnection
from imutils.video import VideoStream
import socket
import window
from Chat.chatHandler import chatHandler
from Groups.groupHandler import groupHandler
from Creatures.CreatureHandler import CreatureHandler
from Creatures.Dice.RollHandler import RollHandler
from ServerHandler.EventHandler import EventHandler
from Initiative.InitiativeHandler import InitiativeHandler


serverIp = "62.163.205.59"

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

    print("initialized server text connection")

    print("initializing group handler")
    group = groupHandler(userName, server.textSender)
    status, groupName = group.createGroup("group", '')
    print("initialized group handler")

    print("initializing creature handler")
    creatures = CreatureHandler(groupName, userName, server.textSender)
    print("initialized creature handler")

    print("initializing chat handler")
    chat = chatHandler(groupName, userName, server.textSender)
    print("initialized chat handler")

    print("initializing initiative handler")
    initiative = InitiativeHandler(groupName, userName, server.textSender)
    print("initialized initiative handler")
    
    print("initializing roll handler")
    rolls = RollHandler(groupName, userName, server.textSender)
    print("initialized roll handler")

    print("added handlers")
    handlers = {
        "group" : group,
        "creatures" : creatures,
        "chat" : chat,
        "initiative" : initiative,
        "rolls" : rolls
    }

    main = window.main(socket.gethostname(), "D&D messaging", server, handlers)

    print("created window")

    eventListener = EventHandler(groupName, userName, server.textSender)
    eventListener.addListener("Message", main.handleMsg)
    eventListener.addListener("Initiative", main.initiativeWindow.handleInitiativeUpdate)
    eventListener.addListener("Start turn", main.initiativeWindow.handleStartTurn)
    eventListener.addListener("Make Roll", rolls.makeRoll)
    print("added event listeners")

    server.start_textLoop(eventListener.HandleEvent)

    print("starting main loop")
    main.start()