import tkinter as tk
import tkinter.ttk as ttk
from Creatures.Actions.Action import Action, Attack, Multiattack, SaveAttack, dc



class ActionWindow(ttk.Frame):

    def __init__(self, action: Action, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.action = action

        ttk.Label(master = self, text = self.action.name).pack()

        desc = tk.Text(master = self, width = 40, height = 4, wrap='word')
        desc.insert(tk.END, self.action.desc)
        desc.config(state = 'disabled')
        desc.pack()

        if len(self.action.damage) > 0:
            ttk.Label(master = self, text = "\nDamage:").pack()
            for dmg in self.action.damage:
                ttk.Label(master = self, text = "type: " + dmg.damage_type).pack()
                ttk.Label(master = self, 
                    text = "dice: " + dmg.damage_dice + "\n").pack()

        if type(self.action) == Multiattack:
            showMultiAttackData(self, self.action)

        if type(self.action) == Attack:
            showAttackData(self, self.action)

        if type(self.action) == SaveAttack:
            showSaveAttackData(self, self.action)


def showMultiAttackData(window: ActionWindow, data: Multiattack) -> None:
    ttk.Label(master = window, text = str(data.num) + " from:")

    for optionList in data.options:
        ttk.Label(master = window, 
            text = " + ".join([option.name for option in optionList]) + ": ").pack()
        for option in optionList:
            ttk.Label(master = window, text = "name: " + option.name).pack()
            ttk.Label(master = window, text = "count: " + str(option.count)).pack()
            ttk.Label(master = window, text = "type: " + option.type + "\n").pack()

def showAttackData(window: ActionWindow, data: Attack) -> None:
    ttk.Label(master = window, 
        text = "attack bonus: " + str(data.attack_bonus) + "\n").pack()
    if data.dc is not None:
        showDC(window, data.dc)

def showSaveAttackData(window: ActionWindow, data: SaveAttack) -> None:
    showDC(window, data.dc)

def showDC(window: ActionWindow, data: dc) -> None:
    ttk.Label(master = window, text = "dc:").pack()
    ttk.Label(master = window, text = "type: " + data.dc_type).pack()
    ttk.Label(master = window, text = "value: " + str(data.dc_value)).pack()
    ttk.Label(master = window, 
        text = "success type: " + data.success_type + "\n").pack()