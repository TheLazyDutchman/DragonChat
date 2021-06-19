import pickle

class groupHandler:

    def __init__(self, userName, sendSocket):
        self.sendSocket = sendSocket
        self.userName = userName

        self.groupName = ''

    def createGroup(self, groupName, password):
        data = pickle.dumps((groupName, password, self.userName))
        self.sendSocket.send_multipart((b"createGroup", data))
        answer = self.sendSocket.recv()
        answer = pickle.loads(answer)

        if answer[0] != "OK":
            return False, answer

        return True, groupName

    def getGroups(self) -> list[str]:
        self.sendSocket.send_multipart((b"getGroups", None))

        groups = self.sendSocket.recv()
        return groups

    def joinGroup(self, groupName, password):
        data = pickle.dumps((groupName, password, self.userName))
        self.sendSocket.send_multipart((b"joinGroup", data))
        answer = self.sendSocket.recv()

        if answer != b"OK":
            return False, answer

        self.groupName = groupName
        return True, answer