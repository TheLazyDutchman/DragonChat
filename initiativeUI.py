import tkinter as tk
import tkinter.ttk as ttk
import random

class initiativeWindow(ttk.Frame):

    def __init__(self, main, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.initiative = list()
        self.listFrame = ttk.Frame(self)

        self.started = False

        self.addCreaturesFrame = self.showAddCreaturesUI()

        self.grid(row=0, column=1, rowspan=2)

    def showAddCreaturesUI(self):
        frame = ttk.Frame(self)

        ttk.Label(frame, text="name").pack()
        creatureName = tk.StringVar()
        ttk.Entry(frame, textvariable=creatureName).pack()

        ttk.Label(frame, text="modifier").pack()
        dexModifier = tk.IntVar()
        ttk.Entry(frame, textvariable=dexModifier).pack()

        ttk.Label(frame, text="number").pack()
        numCreatures = tk.IntVar()
        ttk.Entry(frame, textvariable=numCreatures).pack()

        ttk.Button(frame, text="add creatures", command=lambda : 
            self.AddCreatures(creatureName.get(), numCreatures.get(), dexModifier.get())).pack()

        ttk.Button(frame, text="start initiative", command=self.start).pack()

        frame.grid(column=1, row=0)
        return frame

    def showInInitiativeUI(self):
        frame = ttk.Frame(self)

        ttk.Button(frame, text="next turn", command=self.nextTurn).pack()
        ttk.Button(frame, text="end initiative", command=self.end).pack()

        frame.grid(column=1, row=0)
        return frame

    def start(self):
        self.curCreature = self.initiative[0]
        self.started = True
        self.addCreaturesFrame.grid_remove()
        self.addCreaturesFrame = self.showInInitiativeUI()
        self.sendChanges()

    def end(self):
        self.initiative = list()
        self.started = False
        self.addCreaturesFrame.grid_remove()
        self.addCreaturesFrame = self.showAddCreaturesUI()

    def hasCreatures(self):
        return len(self.initiative) > 0

    def AddCreature(self, name, initiative):
        self.initiative.append((name, int(initiative)))
        self.initiative.sort(key=lambda x: x[1], reverse=True)
        self.curCreature = self.initiative[0]
        self.sendChanges()

    def AddCreatures(self, name, amount, bonus):
        for i in range(int(amount)):
            num = random.randint(1, 20) + int(bonus)
            self.AddCreature(name + str(i), num)

    def RemoveCreature(self, name):
        creature = None
        for c in self.initiative:
            if c[0] == name:
                creature = c
                break
        if creature is self.curCreature:
            index = self.initiative.index(self.curCreature)
            self.curCreature = self.initiative[index + 1]

        if not creature is None:
            self.initiative.remove(c)
        
        self.sendChanges()

    def displayInitiative(self):
        self.listFrame.grid_remove()
        self.listFrame = ttk.Frame(self)
        index = self.initiative.index(self.curCreature)
        initiative = self.initiative[index:]
        initiative.extend(self.initiative[:index])
        for i in range(len(initiative)):
            label = ttk.Label(self.listFrame, text=initiative[i][0] + " : " + str(initiative[i][1]))
            label.grid(row=i, column=0)

        self.listFrame.grid(column=0, row=0)
    
    def nextTurn(self):
        index = self.initiative.index(self.curCreature)
        newIndex = (index + 1) % len(self.initiative)

        self.curCreature = self.initiative[newIndex]
        self.sendChanges()

    def nextTurnPossible(self):
        return self.started

    def getNames(self):
        return [x[0] for x in self.initiative]

    def sendChanges(self):
        self.main.sendMsg(("initiative", self.initiative, self.curCreature))

    def appendChanges(self, initiative, curCreature):
        self.initiative = initiative
        self.curCreature = curCreature
        self.displayInitiative()