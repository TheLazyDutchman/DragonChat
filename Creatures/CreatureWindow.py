from Creatures.CreatureHandler import CreatureHandler
import tkinter as tk
import tkinter.ttk as ttk
import dndApi

class CreatureWindow(ttk.Frame):

    def __init__(self, creatureHandler: CreatureHandler, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.creatureHandler = creatureHandler

        self.creatureList = ttk.Frame(self)
        self.creatureList.grid(column=0, row=0)

        self.monsterList = dndApi.searchMonster('')['results']
        self.monsterList : list[tuple[str, str]] = [(x['name'], x['url']) for x in self.monsterList]

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
            command=lambda: self.createCreature(name.get())).pack()

        def showMonsterOptions(*args):
            data = searchName.get().lower()
            monsterValues.clear()
            monsterValues.extend([(x[0], x[1]) for x in self.monsterList if data in x[0].lower()])
            monsterOptions['values'] = [x[0] for x in monsterValues]
            monsterOptions.current(0)

        showMonsterOptions()

        searchName.trace('w', showMonsterOptions)
            
    def handleServerCreatures(self, data):
        self.creatureList.grid_forget()
        self.creatureList = ttk.Frame(self)
        self.creatureList.grid(column=0, row=0)

        for controller, creature in data:
            ttk.Label(master=self.creatureList, 
                text=f"{creature}: {controller}").pack()

    def createCreature(self, creatureName):
        self.creatureHandler.addCreature(creatureName)