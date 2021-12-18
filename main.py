import socket
import window
from Chat.chatHandler import chatHandler
from Creatures.creatureHandler import CreatureHandler
from Dice.diceHandler import DiceHandler
from Initiative.InitiativeHandler import InitiativeHandler


from pyzmqServer.client import Client

serverIp = "192.168.1.71"

eventPort = 5558
requestSendPort = 5557
requestRecievePort = 5556

groupName = "main"
userName = "client"

connection = Client(serverIp, eventPort, requestSendPort, requestRecievePort)
print("initialized server text connection")


connection.Subscribe(groupName.encode('utf-8'))
connection.Subscribe(userName.encode('utf-8'))


print("initializing chat handler")
chat = chatHandler(groupName, userName, connection)
print("initialized chat handler")

print("initializing initiative handler")
initiative = InitiativeHandler(groupName, userName, connection)
print("initialized initiative handler")

print("initializing roll handler")
rolls = DiceHandler(groupName, userName, connection)
print("initialized roll handler")

print("added handlers")
handlers = {
    "chat" : chat,
    "initiative" : initiative
}

main = window.main(socket.gethostname(), "D&D messaging", handlers, connection)


rolls.setMaster(main)

print("created window")

connection.addEventType("message")
connection.setEventHandler("message", main.handleMsg)

connection.createTkinterRequestLoop("UI loop", main)
connection.addRequestType("make roll")
connection.setRequestHandler("make roll", rolls.handleRoll, "UI loop")

print("added event listeners")

print("starting main loop")
main.start()