import pickle

class Handler:

    def __init__(self, groupName: str, userName: str, sendSocket):
        self.groupName = groupName
        self.userName = userName
        self.sendSocket = sendSocket

    def SendServerMessage(self, messageType: str, data: tuple) -> list:
        data = pickle.dumps(data)
        self.sendSocket.send_multipart((messageType.encode("utf-8"), data))
        answer = self.sendSocket.recv()
        return pickle.loads(answer)
