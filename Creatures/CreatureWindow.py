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


        dataNoteBook = ttk.Notebook(master = self)

        actionsWindow = ScrollableFrame(dataNoteBook)

        print(self.creature)

        dataNoteBook.add(actionsWindow, text="actions")
        dataNoteBook.pack()
        for action in self.creature.actions:
            actionFrame = ActionWindow(
                action,
                self.creature.id,
                self.creatureHandler,
                master = actionsWindow.scrollable_frame)
            actionFrame.pack()
            actionsWindow.bind(actionFrame)