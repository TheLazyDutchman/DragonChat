from ServerHandler.Handler import Handler

class chatHandler(Handler):

    def sendMessage(self, message):
        self.connection.SendRequest("message", message)