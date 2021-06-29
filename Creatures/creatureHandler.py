from ServerHandler.Handler import Handler
class creatureHandler(Handler):

    def addCreature(self, creatureName):
        creatureData = {
            "name": creatureName,
            "controller": self.userName
        }
        data = (self.groupName, creatureData)

        answer = self.SendServerMessage("addCreature", data)

        if answer[0] != "OK" or not str(answer[0]).isnumeric():
            return False, answer

        return True, answer