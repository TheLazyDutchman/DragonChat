import tkinter.ttk as ttk

from DandData.dice import Roll



class DiceFrame(ttk.Frame):

    def __init__(self, master, roll: Roll) -> None:
        super().__init__(master)
        self.roll = roll

        ttk.Label(self, text = self.roll).pack()