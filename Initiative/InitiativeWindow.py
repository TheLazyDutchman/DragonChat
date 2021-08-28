from Creatures.CreatureWindow import CreatureWindow
import tkinter.ttk as ttk
from Initiative.InitiativeHandler import InitiativeHandler

class InitiativeWindow(ttk.Frame):

    def __init__(self, initiativeHandler: InitiativeHandler, master = None, *args, **kwargs):
        super().__init__(master=master, *args, **kwargs)

        self.initiativeHandler = initiativeHandler

        self.initiativeList = ttk.Frame(self)

        ttk.Button(self, text="Start initiative", 
            command=self.startInitiative).grid(column=1, row=0)
        ttk.Button(self, text="Next turn", 
            command=self.nextTurn).grid(column=1, row=1)

        self.currentCreatureWindow = ttk.Frame(self)

    def startInitiative(self):
        self.initiativeHandler.StartInitiative()

    def nextTurn(self):
        self.initiativeHandler.NextTurn()

    def handleInitiativeUpdate(self, data):
        self.initiativeList.grid_forget()
        self.initiativeList = ttk.Frame(self)
        self.initiativeList.grid(column=0, row=0, rowspan=2)

        for (controller, creature), initiative in data:
            ttk.Label(master=self.initiativeList, 
                text=f"{creature}: {controller}: {initiative}").pack()

    def handleStartTurn(self, data):
        print(data)

        self.currentCreatureWindow.grid_forget()

        self.currentCreatureWindow = CreatureWindow(data, self.initiativeHandler, self)
        self.currentCreatureWindow.grid(column=2, row=0, rowspan=2)