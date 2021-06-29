from ServerHandler.Handler import Handler

class groupHandler(Handler):

    def __init__(self, userName, sendSocket):
        super().__init__('', userName, sendSocket)

    def createGroup(self, groupName, password):
        data = (groupName, password, self.userName)
        answer = self.SendServerMessage("createGroup", data)

        if answer[0] != "OK":
            if answer[0] == "group already exists":
                return self.joinGroup(groupName, password)

            return False, answer

        return True, groupName

    def getGroups(self) -> list[str]:
        self.sendSocket.send_multipart((b"getGroups", None))

        groups = self.sendSocket.recv()
        return groups

    def joinGroup(self, groupName, password):
        data = (groupName, password, self.userName)
        answer = self.SendServerMessage("joinGroup", data)

        if answer[0] != "OK":
            return False, answer

        return True, groupName