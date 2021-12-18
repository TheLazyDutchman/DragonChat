from ServerHandler.Handler import Handler

class chatHandler(Handler):

    def sendMessage(self, message):
        data = (self.connection.groupName, self.connection.clientName, message)
        self.connection.SendRequest("message", data)