import tkinter as tk

from ServerHandler.Handler import Handler
from DandData.dice import Roll

from .diceFrame import DiceFrame



class DiceHandler(Handler):

    def setMaster(self, master):
        self.master = master
    
    def handleRoll(self, rolls: tuple[tuple[str, Roll], ...]):
        answer = []

        window = tk.Toplevel(master=self.master)
        window.title("Roll dice")
        for name, roll in rolls:
            
            DiceFrame(window, name, roll).pack()

        return answer