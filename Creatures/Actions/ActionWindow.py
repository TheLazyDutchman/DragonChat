from DandData.action import Action, Attack, MultiAttack

import tkinter as tk
import tkinter.ttk as ttk
from Creatures.creatureHandler import CreatureHandler



class ActionWindow(ttk.Frame):

    def __init__(self, action: Action, creatureId: int, creatureHandler: CreatureHandler, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.action = action
        self.creatureId = creatureId
        self.creatureHandler = creatureHandler

        ttk.Label(master = self, text = self.action.name).pack()

        desc = tk.Text(master = self, width = 40, height = 4, wrap='word')
        desc.insert(tk.END, self.action.desc)
        desc.config(state = 'disabled')
        desc.pack()

        if len(self.action.damage) > 0:
            ttk.Label(master = self, text = "\nDamage:").pack()
            for dmg in self.action.damage:
                ttk.Label(master = self, text = f"type: {dmg.dmgType.name}").pack()
                ttk.Label(master = self, 
                    text = f"dice: {dmg.dice}\n").pack()

        if type(self.action) == MultiAttack:
            showMultiAttackData(self, self.action)

        if type(self.action) == Attack:
            showAttackData(self, self.action)

        # if type(self.action) == SaveAttack:
        #     showSaveAttackData(self, self.action)

        ttk.Button(master = self, text = "Use", command = self.Use).pack()

    def Use(self):
        self.creatureHandler.UseAction(self.creatureId, self.action)


def showMultiAttackData(window: ActionWindow, data: MultiAttack) -> None:
    for option in data.options:
        ttk.Label(master = window, text = "name: " + option.name).pack()
        ttk.Label(master = window, text = "count: " + str(option.count)).pack()
        ttk.Label(master = window, text = "type: " + option.actionType + "\n").pack()

def showAttackData(window: ActionWindow, data: Attack) -> None:
    ttk.Label(master = window, 
        text = "attack bonus: " + str(data.attack_bonus) + "\n").pack()

# def showSaveAttackData(window: ActionWindow, data: SaveAttack) -> None:
#     showDC(window, data.dc)

# def showDC(window: ActionWindow, data: dc) -> None:
#     ttk.Label(master = window, text = "dc:").pack()
#     ttk.Label(master = window, text = "type: " + data.dc_type).pack()
#     ttk.Label(master = window, text = "value: " + str(data.dc_value)).pack()
#     ttk.Label(master = window, 
#         text = "success type: " + data.success_type + "\n").pack()