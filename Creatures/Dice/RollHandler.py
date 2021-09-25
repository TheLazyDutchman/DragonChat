from pyzmqServer.client import Client

from ServerHandler.Handler import Handler
from Creatures.Dice.Roll import Roll



class RollHandler(Handler):

    def __init__(self, groupName: str, userName: str, connection: Client) -> None:
        super().__init__(groupName, userName, connection)
        self.connection.AddRequestListener("make roll", self.HandleRoll)


    def HandleRoll(self, event) -> None:
        roll: Roll = event

        print(roll)