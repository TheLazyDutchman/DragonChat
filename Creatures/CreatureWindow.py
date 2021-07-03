from Creatures.CreatureHandler import CreatureHandler
import tkinter as tk
import tkinter.ttk as ttk

class CreatureWindow(ttk.Frame):

    def __init__(self, creatureHandler: CreatureHandler, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.creatureHandler = creatureHandler

        self.creatureList = ttk.Frame(self)
        self.creatureList.grid(column=0, row=0)

        self.drawInputUI()

    def drawInputUI(self):
        addCreatureInput = ttk.Frame(self)
        addCreatureInput.grid(column=1, row=0)

        name = tk.StringVar(self)
        ttk.Entry(master=addCreatureInput, textvariable=name).pack()
        ttk.Button(master=addCreatureInput, 
            text="Add Creature", 
            command=lambda: self.createCreature(name.get())).pack()

    def handleServerCreatures(self, data):
        self.creatureList.grid_forget()
        self.creatureList = ttk.Frame(self)
        self.creatureList.grid(column=0, row=0)

        for controller, creature in data:
            ttk.Label(master=self.creatureList, 
                text=f"{creature}: {controller}").pack()

    def createCreature(self, creatureName):
        self.creatureHandler.addCreature(creatureName)