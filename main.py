import ClientConnection
from imutils.video import VideoStream
import socket
import window
from Chat.chatHandler import chatHandler
from Groups.groupHandler import groupHandler
from Creatures.creatureHandler import creatureHandler


serverIp = "212.187.9.198"
imgSendPort = 5555
imgRecvPort = 5556
textSendPort = 5557
textRecvPort = 5558
soundSendPort = 5559
soundRecvPort = 5560

camera = VideoStream().start()

with ClientConnection.Connections(socket.gethostname(), "group", serverIp) as server:
    server.initialize_text_data(textSendPort, textRecvPort)

    group = groupHandler(serverIp, server.textSender)
    status, groupName = group.createGroup("group", '')

    print(status, groupName)

    creatures = creatureHandler(groupName, serverIp, server.textSender)

    chat = chatHandler("group", serverIp, server.textSender)

    handlers = {
        "group" : group,
        "creatures" : creatures,
        "chat" : chat
    }

    main = window.main(socket.gethostname(), "D&D messaging", server, handlers)

    server.start_textLoop(main.handleMsg)

    main.start()