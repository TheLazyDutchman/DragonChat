from Initiative.InitiativeHandler import InitiativeHandler
import tkinter.ttk as ttk

class CreatureWindow(ttk.Frame):

    def __init__(self, creature: dict, initiativeHandler: InitiativeHandler, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.initiativeHandler = initiativeHandler

        ttk.Label(master=self, text=creature['name']).pack()