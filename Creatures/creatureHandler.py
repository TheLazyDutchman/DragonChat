from ServerHandler.Handler import Handler
class CreatureHandler(Handler):

    def addCreature(self, creatureType: str):
        data = (self.groupName, self.userName, creatureType)
        print("adding creature", creatureType)

        answer = self.SendServerMessage("addCreature", data)

        return answer[0]