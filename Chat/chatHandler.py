from ServerHandler.Handler import Handler

class chatHandler(Handler):

    def sendMessage(self, message):
        data = (self.groupName, self.userName, message)
        self.connection.SendRequest("message", data)