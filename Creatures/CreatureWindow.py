from Creatures.Actions.ActionWindow import ActionWindow
from Initiative.InitiativeHandler import InitiativeHandler
import tkinter.ttk as ttk
from Creatures.Actions.Action import ActionFactory
from ScrollableFrame import ScrollableFrame

class CreatureWindow(ttk.Frame):
    actionFactory = ActionFactory()

    def __init__(self, creature: dict, initiativeHandler: InitiativeHandler, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.initiativeHandler = initiativeHandler
        ttk.Label(master=self, text=creature['name']).pack()


        dataNoteBook = ttk.Notebook(master = self)

        actionsWindow = ScrollableFrame(dataNoteBook)

        dataNoteBook.add(actionsWindow, text="actions")
        dataNoteBook.pack()
        for action in creature["actions"]:
            actionFrame = ActionWindow(
                self.actionFactory.Create(action), 
                master = actionsWindow.scrollable_frame)
            actionFrame.pack()
            actionsWindow.bind(actionFrame)