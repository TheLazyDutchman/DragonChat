from ServerHandler.Handler import Handler
class CreatureHandler(Handler):

    def addCreature(self, creatureType: str):
        data = (self.groupName, self.userName, creatureType)
        print("adding creature", creatureType)

        answer = self.SendServerMessage("addCreature", data)

        if answer[0] != "OK" or not str(answer[0]).isnumeric():
            return False, answer

        return True, answer