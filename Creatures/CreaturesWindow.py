from Creatures.CreatureWindow import CreatureWindow
from Creatures.creatureHandler import CreatureHandler
import tkinter as tk
import tkinter.ttk as ttk
import dndApi

class CreaturesWindow(ttk.Frame):

    def __init__(self, creatureHandler: CreatureHandler, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.creatureHandler = creatureHandler

        self.creatureNoteBook = ttk.Notebook(master = self)
        self.creatureNoteBook.grid(column=0, row=0)

        self.monsterList = dndApi.searchMonster('')['results']
        self.monsterList : list[tuple[str, str]] = [(x['name'], x['index']) for x in self.monsterList]

        self.drawInputUI()

    def drawInputUI(self):
        addCreatureInput = ttk.Frame(self)
        addCreatureInput.grid(column=1, row=0)

        searchName = tk.StringVar(self)
        ttk.Entry(master=addCreatureInput, textvariable=searchName).pack()

        name = tk.StringVar(self)
        monsterOptions = ttk.Combobox(master=addCreatureInput, textvariable=name)
        monsterOptions.pack()

        monsterValues = list()

        ttk.Button(master=addCreatureInput, 
            text="Add Creature", 
            command=lambda: self.createCreature([monster[1] for monster in monsterValues if monster[0] == name.get()][0])).pack()

        def showMonsterOptions(*args):
            data = searchName.get().lower()
            monsterValues.clear()
            monsterValues.extend([(x[0], x[1]) for x in self.monsterList if data in x[0].lower()])
            monsterOptions['values'] = [x[0] for x in monsterValues]
            monsterOptions.current(0)

        showMonsterOptions()

        searchName.trace('w', showMonsterOptions)
            
    def createCreature(self, creatureName):
        creature: dict = self.creatureHandler.addCreature(creatureName)

        creatureWindow = CreatureWindow(creature, self.creatureHandler, master = self.creatureNoteBook)

        self.creatureNoteBook.add(creatureWindow, text=creature["name"])