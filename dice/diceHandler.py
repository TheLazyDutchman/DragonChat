import tkinter as tk

from ServerHandler.Handler import Handler
from DandData.dice import Roll

from .diceFrame import DiceFrame



class DiceHandler(Handler):

    def setMaster(self, master):
        self.master = master
    
    def handleRoll(self, rolls: dict[str, Roll]):
        result: dict[str, int] = {}

        def addResult(name: str, value: int) -> None:
            result[name] = value

            print(result)

        window = tk.Toplevel(master=self.master)
        window.title("Roll dice")

        for name, roll in rolls.items():
            DiceFrame(window, name, roll, addResult).pack()
