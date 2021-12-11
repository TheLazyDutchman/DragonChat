from DandData.creature import Creature

from Creatures.creatureHandler import CreatureHandler
from Creatures.Actions.ActionWindow import ActionWindow
import tkinter.ttk as ttk
from ScrollableFrame import ScrollableFrame



class CreatureWindow(ttk.Frame):

    def __init__(self, creature: Creature, creatureHandler: CreatureHandler, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.creature = creature
        self.creatureHandler = creatureHandler

        ttk.Label(master=self, text=creature.name).pack()


        self.dataNoteBook = ttk.Notebook(master = self)
        self.dataNoteBook.pack(fill = 'both', expand = True)

        self.showStats()
        self.showActions()

    def showStats(self):
        statsWindow = ScrollableFrame(self.dataNoteBook)
        statsWindow.pack(fill = 'both', expand = True)

        ttk.Label(statsWindow.scrollable_frame, text = f"Name: {self.creature.name}").pack()
        ttk.Label(statsWindow.scrollable_frame, text = f"AC: {self.creature.armorClass}").pack()
        ttk.Label(statsWindow.scrollable_frame, text = f"Health: {self.creature.health}/{self.creature.hitPoints}").pack()

        self.dataNoteBook.add(statsWindow, text="stats")
    
    def showActions(self):
        actionsWindow = ScrollableFrame(self.dataNoteBook)
        actionsWindow.pack(fill = 'both', expand = True)

        for action in self.creature.actions:
            actionFrame = ActionWindow(
                action,
                self.creature.id,
                self.creatureHandler,
                master = actionsWindow.scrollable_frame)
            actionFrame.pack()
            actionsWindow.bind(actionFrame)

        self.dataNoteBook.add(actionsWindow, text="actions")