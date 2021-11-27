import tkinter as tk
import tkinter.ttk as ttk
from typing import Callable

from DandData.dice import Roll



class DiceFrame(ttk.Frame):

    def __init__(self, master, name: str, roll: Roll, returnFunction: Callable[[str, int], None]) -> None:
        super().__init__(master)
        self.roll = roll
        self.name = name
        self.input = tk.IntVar()
        self.returnFunction = returnFunction

        ttk.Label(self, text = self.name).pack()
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

        self.returnFunction(self.name, amount)