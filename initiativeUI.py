import tkinter as tk
import tkinter.ttk as ttk
import random

class initiativeWindow(ttk.Frame):

    def __init__(self, main, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.grid(row=0, column=1, rowspan=2)
        self.initiative = list()

        self.started = False

    def start(self):
        self.curCreature = self.initiative[0]
        self.started = True
        self.sendChanges()

    def hasCreatures(self):
        return len(self.initiative) > 0

    def AddCreature(self, name, initiative):
        self.initiative.append((name, int(initiative)))
        self.initiative.sort(key=lambda x: x[1], reverse=True)
        if not self.started:
            self.start()
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
        index = self.initiative.index(self.curCreature)
        initiative = self.initiative[index:]
        initiative.extend(self.initiative[:index])
        for i in range(len(initiative)):
            label = ttk.Label(self, text=initiative[i][0] + " : " + str(initiative[i][1]))
            label.grid(row=i, column=0)
    
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