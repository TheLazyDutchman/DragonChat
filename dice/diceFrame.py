import tkinter as tk
import tkinter.ttk as ttk

from DandData.dice import Roll



class DiceFrame(ttk.Frame):

    def __init__(self, master, roll: Roll) -> None:
        super().__init__(master)
        self.roll = roll
        self.input = tk.IntVar()

        ttk.Label(self, text = self.roll).pack()

        ttk.Entry(self, textvariable = self.input).pack()
        ttk.Button(self, text = "Apply input", command = self.applyInput).pack()

    def applyInput(self):
        amount = self.input.get()

        if (amount < self.roll.getMinRoll()):
            print(f"{self.roll} can not roll lower than {self.roll.getMinRoll()}")
            return
        if (amount > self.roll.getMaxRoll()):
            print(f"{self.roll} can not roll higher than {self.roll.getMaxRoll()}")
            return

        print(self.input.get())