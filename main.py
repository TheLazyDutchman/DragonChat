import socket
import window
from Chat.chatHandler import chatHandler
from Groups.groupHandler import groupHandler
from Creatures.CreatureHandler import CreatureHandler
from ServerHandler.EventHandler import EventHandler
from Initiative.InitiativeHandler import InitiativeHandler


from pyzmqServer.client import Client

serverIp = "192.168.1.71"

eventPort = 5558
requestSendPort = 5557
requestRecievePort = 5558

userName = "testUser"

connection = Client(serverIp, eventPort, requestSendPort, requestRecievePort)
print("initialized server text connection")



print("initializing group handler")
group = groupHandler(userName, connection)
status, groupName = group.createGroup("group", '')
print("initialized group handler")

connection.Subscribe(groupName.encode('utf-8'))
connection.Subscribe(userName.encode('utf-8'))

print("initializing creature handler")
creatures = CreatureHandler(groupName, userName, connection)
print("initialized creature handler")

print("initializing chat handler")
chat = chatHandler(groupName, userName, connection)
print("initialized chat handler")

print("initializing initiative handler")
initiative = InitiativeHandler(groupName, userName, connection)
print("initialized initiative handler")

# print("initializing roll handler")
# rolls = RollHandler(groupName, userName, connection)
# print("initialized roll handler")

print("added handlers")
handlers = {
    "group" : group,
    "creatures" : creatures,
    "chat" : chat,
    "initiative" : initiative
}

main = window.main(socket.gethostname(), "D&D messaging", handlers)

print("created window")

eventListener = EventHandler(groupName, userName, connection)
eventListener.addListener("Message", main.handleMsg)
eventListener.addListener("Initiative", main.initiativeWindow.handleInitiativeUpdate)
eventListener.addListener("Start turn", main.initiativeWindow.handleStartTurn)
# eventListener.addListener("Make Roll", rolls.makeRoll)
print("added event listeners")

connection.SetEventCallback(eventListener.HandleEvent)

print("starting main loop")
main.start()