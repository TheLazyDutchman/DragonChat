from ServerHandler.Handler import Handler
class CreatureHandler(Handler):

    def addCreature(self, creatureData):

        # add controller to creature data
        creatureData['controller'] = self.userName

        data = (self.groupName, creatureData)

        answer = self.SendServerMessage("addCreature", data)

        if answer[0] != "OK" or not str(answer[0]).isnumeric():
            return False, answer

        return True, answer