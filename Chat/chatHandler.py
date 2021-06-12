import pickle

class chatHandler:

    def __init__(self, group: str, userName: str, sendSocket):
        self.group = group
        self.userName = userName
        self.sendSocket = sendSocket


    def sendMessage(self, message):
        data = pickle.dumps((self.group, self.userName, message))
        self.sendSocket.send_multipart((b"message", data))

        self.sendSocket.recv()