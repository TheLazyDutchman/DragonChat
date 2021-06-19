import pickle

class creatureHandler:

    def __init__(self, groupdName, userName, sendSocket):
        self.groupdName = groupdName
        self.userName = userName
        self.sendSocket = sendSocket

    def addCreature(self, creatureName):
        data = pickle.dumps((self.groupdName, self.userName, creatureName))

        self.sendSocket.send_multipart((b"addCreature", data))
        answer = self.sendSocket.recv()

        if answer != b"OK" or not str(answer).isnumeric():
            return False, answer

        return True, answer