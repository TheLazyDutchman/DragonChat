from ServerHandler.Handler import Handler

class InitiativeHandler(Handler):

    def StartInitiative(self):
        data = self.groupName

        answer = self.connection.SendRequest("StartInitiative", data)

    def NextTurn(self):
        data = self.groupName

        answer = self.connection.SendRequest("NextTurn", data)