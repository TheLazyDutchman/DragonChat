import pickle

class creatureHandler:

    def __init__(self, groupName, userName, sendSocket):
        self.groupName = groupName
        self.userName = userName
        self.sendSocket = sendSocket

    def addCreature(self, creatureName):
        data = pickle.dumps((self.groupName, self.userName, creatureName))

        self.sendSocket.send_multipart((b"addCreature", data))
        answer = self.sendSocket.recv()

        if answer != b"OK" or not str(answer).isnumeric():
            return False, answer

        return True, answer