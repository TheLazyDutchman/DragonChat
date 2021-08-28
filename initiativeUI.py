import pickle
import tkinter as tk
import tkinter.ttk as ttk
import random
from dndApi import searchMonster, getMonster

class initiativeWindow(ttk.Frame):

    def __init__(self, main, parent, creatureHandler, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.initiative = list()
        self.listFrame = ttk.Frame(self)

        self.started = False

        self.creatureHandler = creatureHandler

        self.addCreaturesFrame = self.showAddMonstersUI()

        self.grid(row=0, column=1, rowspan=2)

    def showAddMonstersUI(self):
        monsters = searchMonster('')['results']
        monsters = [(x['name'], x['url']) for x in monsters]
        frame = ttk.Frame(self)

        ttk.Label(frame, text="name").pack()
        name = tk.StringVar()
        ttk.Entry(frame, textvariable=name).pack()
        monsterName = tk.StringVar()

        monsterOptions = ttk.Combobox(frame, textvariable=monsterName)
        monsterOptions.pack()

        values = list()

        ttk.Label(frame, text="number").pack()
        numCreatures = tk.IntVar()
        ttk.Entry(frame, textvariable=numCreatures).pack()

        ttk.Button(frame, text="add creatures", command=lambda : 
            self.AddMonster(values[monsterOptions.current()][1])).pack()

        ttk.Button(frame, text="start initiative", command=self.start).pack()


        def showMonsterOptions(*args):
            data = name.get().lower()
            values.clear()
            values.extend([(x[0], x[1]) for x in monsters if data in x[0].lower()])
            monsterOptions['values'] = [x[0] for x in values]
            monsterOptions.current(0)

        showMonsterOptions() # show all monsters on default

        name.trace('w', showMonsterOptions)

        frame.grid(column=1, row=0)
        return frame

    def showInInitiativeUI(self):
        frame = ttk.Frame(self)

        ttk.Button(frame, text="next turn", command=self.nextTurn).pack()
        ttk.Button(frame, text="end initiative", command=self.end).pack()

        frame.grid(column=1, row=0)
        return frame

    def start(self):
        data = pickle.dumps((self.creatureHandler.groupName))
        self.creatureHandler.sendSocket.send_multipart((b"StartInitiative", data))
        self.creatureHandler.sendSocket.recv()

        self.addCreaturesFrame.grid_remove()
        self.addCreaturesFrame = self.showInInitiativeUI()

    def end(self):
        self.initiative = list()
        self.started = False
        self.addCreaturesFrame.grid_remove()
        self.addCreaturesFrame = self.showAddMonstersUI()

    def nextTurn(self):
        data = pickle.dumps((self.creatureHandler.groupName))
        self.creatureHandler.sendSocket.send_multipart((b"NextTurn", data))
        self.creatureHandler.sendSocket.recv()

    def hasCreatures(self):
        return len(self.initiative) > 0

    def AddCreature(self, name, initiative):
        self.creatureHandler.addCreature(name)

    def AddMonster(self, name):
        monster = getMonster(name)
        self.AddCreature(monster.name, 0)

    def ShowInitiative(self, initiativeList: list[tuple[str, str]]):
        self.listFrame.grid_remove()
        self.listFrame = ttk.Frame(self)

        for userName, creature, initiative in initiativeList:
            ttk.Label(self.listFrame, text=f"{creature}: {userName}: {initiative}").pack()

        self.listFrame.grid(column=0, row=0)