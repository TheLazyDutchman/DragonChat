from Creatures.Actions.Action import Action
from ServerHandler.Handler import Handler
class CreatureHandler(Handler):

    def addCreature(self, creatureType: str):
        data = (self.groupName, self.userName, creatureType)
        print("Adding creature", creatureType)

        answer = self.connection.SendRequest("add creature", data)

        return answer

    def UseAction(self, creatureId: int, action: Action):
        data = (self.groupName, self.userName, creatureId, action.name)
        print("Using action", action.name)

        answer = self.connection.SendRequest("use action", data)

        return answer