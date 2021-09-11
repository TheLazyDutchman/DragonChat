from pyzmqServer.client import Client

class Handler:

    def __init__(self, groupName: str, userName: str, connection: Client):
        self.groupName = groupName
        self.userName = userName
        self.connection = connection