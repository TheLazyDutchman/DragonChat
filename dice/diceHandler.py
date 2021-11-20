from ServerHandler.Handler import Handler
from DandData.dice import Roll

import tkinter as tk



class DiceHandler(Handler):

    def setMaster(self, master):
        self.master = master
    
    def handleRoll(self, rolls: tuple[Roll, ...]):
        answer = []

        window = tk.Toplevel(master=self.master)
        window.title("Roll dice")
        for roll in rolls:
            answer.append(roll.amount * int(roll.dice_type) + roll.bonus)

        return answer