from pyzmqServer.client import Client

class Handler:

    def __init__(self, connection: Client):
        self.connection = connection