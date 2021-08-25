from Creatures.Actions.ActionWindow import ActionWindow
from Initiative.InitiativeHandler import InitiativeHandler
import tkinter.ttk as ttk
from Creatures.Actions.Action import ActionFactory

class CreatureWindow(ttk.Frame):
    actionFactory = ActionFactory()

    def __init__(self, creature: dict, initiativeHandler: InitiativeHandler, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.initiativeHandler = initiativeHandler

        ttk.Label(master=self, text=creature['name']).pack()
        for action in creature["actions"]:
            ActionWindow(self.actionFactory.Create(action), master = self).pack()