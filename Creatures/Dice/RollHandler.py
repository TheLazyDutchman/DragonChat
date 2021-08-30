from ServerHandler.Handler import Handler
from Creatures.Dice.Roll import Roll



class RollHandler(Handler):

    def makeRoll(self, roll: Roll) -> None:
        print(roll)