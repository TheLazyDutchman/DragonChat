from ServerHandler.Handler import Handler

class InitiativeHandler(Handler):

    def StartInitiative(self):
        data = self.groupName

        answer = self.SendServerMessage("StartInitiative", data)

    def NextTurn(self):
        data = self.groupName

        answer = self.SendServerMessage("NextTurn", data)