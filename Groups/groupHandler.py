from ServerHandler.Handler import Handler

class groupHandler(Handler):

    def __init__(self, userName, connection):
        super().__init__('', userName, connection)

    def createGroup(self, groupName, password):
        data = (groupName, password, self.userName)
        answer = self.connection.SendRequest("createGroup", data)

        if answer[0] != "OK":
            if answer[0] == "group already exists":
                return self.joinGroup(groupName, password)

            return False, answer

        return True, groupName

    def joinGroup(self, groupName, password):
        data = (groupName, password, self.userName)
        answer = self.connection.SendRequest("joinGroup", data)

        if answer[0] != "OK":
            return False, answer

        return True, groupName