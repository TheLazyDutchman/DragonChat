from DandData.creature import Creature
from pyzmqServer.client import Client

from Creatures.Actions.Action import Action
from ServerHandler.Handler import Handler



class CreatureHandler(Handler):

    def __init__(self, groupName: str, userName: str, connection: Client) -> None:
        super().__init__(groupName, userName, connection)

        connection.addRequestType("show creature")

    def addCreature(self, creatureType: str):
        data = (self.groupName, self.userName, creatureType)
        print("Adding creature", creatureType)

        answer = self.connection.SendRequest("add creature", data)

        if answer[0] == False:
            print("could not create creature: '", answer[1], "'")

    def UseAction(self, creatureId: int, action: Action) -> Creature:
        data = (self.groupName, self.userName, creatureId, action.name)
        print("Using action", action.name)

        answer: Creature = self.connection.SendRequest("use action", data)

        return answer