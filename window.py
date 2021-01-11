import tkinter as tk
import tkinter.ttk as ttk
from cv2 import cv2
from PIL import Image, ImageTk
import dndApi
import random
from userCommands import command, commandGroup
import time

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.objAmount = 0

        self.canvas.bind("<MouseWheel>", self.mouse_wheel) # Windows mouse wheel event
        self.canvas.bind("<Button-4>", self.mouse_wheel) # Linux mouse wheel event (Up)
        self.canvas.bind("<Button-5>", self.mouse_wheel) # Linux mouse wheel event (Down)

        self.scrollable_frame.bind("<MouseWheel>", self.mouse_wheel) # Windows mouse wheel event
        self.scrollable_frame.bind("<Button-4>", self.mouse_wheel) # Linux mouse wheel event (Up)
        self.scrollable_frame.bind("<Button-5>", self.mouse_wheel) # Linux mouse wheel event (Down)

    def mouse_wheel(self, event):
        """ Mouse wheel as scroll bar """
        direction = 0
        # respond to Linux or Windows wheel event
        if event.num == 5 or event.delta == -120:
            direction = 1
        if event.num == 4 or event.delta == 120:
            direction = -1
        self.canvas.yview_scroll(direction, "units")

    def clearFrame(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        self.objAmount = 0

    def bindObj(self, obj):
        obj.grid(row=self.objAmount, column = 0, sticky="NW")
        self.objAmount += 1

        obj.bind("<MouseWheel>", self.mouse_wheel) # Windows mouse wheel event
        obj.bind("<Button-4>", self.mouse_wheel) # Linux mouse wheel event (Up)
        obj.bind("<Button-5>", self.mouse_wheel) # Linux mouse wheel event (Down)

# the window for the videos----------------------------------------------------

class videoWindow(ttk.Label):

    def __init__(self, ref main, parent, pos, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.grid(row=pos[0], column=pos[1])

    def displayFrame(self, frame):
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(image)
        imgTK = ImageTk.PhotoImage(image=img)

        self.imgtk = imgTK
        self.configure(image=imgTK)

class videosWindow(ttk.Frame):

    def __init__(self,ref main, parent, server, maxWidth, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main
        self.server = server
        self.maxWidth = maxWidth

        self.grid(row=0, column=0)

        self.videoWindows = dict()

        self.after(15, func=self.updateFrames)

    def updateFrames(self):
        frames = self.server.recv_images()

        values = self.videoWindows.values()
        for _, lastUpdate in values:
            lastUpdate += 1

        items = frames.items()
        yindex = 0
        xindex = 0
        for name, frame in items:
            if not name in self.videoWindows:
                lastUpdate = 0
                self.videoWindows[name] = (videoWindow(self.main, self, (yindex, xindex)), lastUpdate)

            xindex += 1
            if xindex >= self.maxWidth:
                xindex = 0
                yindex += 1

            self.videoWindows[name][0].displayFrame(frame)
            self.videoWindows[name] = (self.videoWindows[name][0], 0)
        
        items = self.videoWindows.items()
        for name, (window, lastUpdate) in items:
            if lastUpdate > 10:
                window.window.destroy()
                self.videoWindows.pop(name)

        self.after(100, func=self.updateFrames)

# the window for the text-----------------------------------------------------

class textWindow(ttk.Frame):

    def __init__(self,ref main, parent, chatSendCallback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main
        self.commands = dict()

        self.grid(row=0, column=1)

        self.chat = chatWindow(self.main, self, chatSendCallback)
        self.rules = rulesWindow(self.main, self)
        self.initiative = initiativeWindow(self.main, self)

# the windows for the chat----------------------------------------------------

class chatTextWindow(ScrollableFrame):

    def __init__(self,ref main, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.grid(row=0, column=0)

    def displayMessage(self, message):
        self.bindObj(ttk.Label(self.scrollable_frame, text=message[0] + " : " + message[1]))
        time.sleep(0.01)
        self.canvas.yview_moveto(1)

class chatInputWindow(ttk.Frame):

    def __init__(self,ref main, parent, callBack, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.grid(row=1, column=0)
        self.callBack = callBack

        self.textVar = tk.StringVar(self)
        def textChange(a, b, c):
            data = self.textVar.get()
            if len(data) > 0:
                if data[0] == "!":
                    data = data[1:]

                    options = self.main.getCommandOptions(data)
                    self.set_options(options)



        self.textVar.trace('w', textChange)

        self.input = ttk.Entry(self, textvariable=self.textVar)
        self.input.grid(row=0, column=0)

        self.submit = ttk.Button(self, text="send", command=self.send_text)
        self.submit.grid(row=0, column=1)

    def send_text(self):
        text = self.input.get()
        if not len(text) == 0:
            if not text[0] == "!":
                self.callBack(("msg", self.main.name, text))
            else:
                self.main.testStringWithCommands(text[1:])
            
            self.input.delete(0, len(text))

    def set_options(self, options):
        # options are stored in key value pairs, like (key, value)
        var = tk.StringVar()
        self.optnListBox = ttk.OptionMenu(self, var, "Select", *[opt[0] for opt in options])
        self.optnListBox.grid(row=1, column=0)

        def select(a, b, c):
            name = var.get()
            selection = [opt for opt in options if opt[0] == name][0]

            self.input.delete(0, len(self.input.get()))
            self.input.insert(tk.END, selection[1])

            self.optnListBox.after(15, func=self.optnListBox.destroy)

            if selection[2]:
                self.submit.invoke()

        var.trace("w", select)

class chatWindow(ttk.Frame):

    def __init__(self,ref main, parent, textCallBack, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.text = chatTextWindow(self.main, self)
        self.input = chatInputWindow(self.main, self, textCallBack)

        self.grid(row=0, column=0, )

    def handleMsg(self, msg):
        if msg[0] == "msg":
            self.text.displayMessage(msg[1:])
        if msg[0] == "initiative":
            self.main.appendInitiativeChanges(msg[1], msg[2])

# the window for the dnd rules--------------------------------------------------

class rulesWindow(ttk.Frame):
    
    def __init__(self,ref main, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main
        self.grid(row=1, column=0)

        self.title = ttk.Label(self, text="rules")
        self.title.pack()

        self.text = ScrollableFrame(self)
        self.text.pack()

        self.main.addChatCommandGroup("rule")
        self.main.addChatCommand("rule", "check", self.displayRule, ("rule",))

    def displayRule(self, rule):
        self.text.clearFrame()

        if type(rule) == dict:
            rule = rule['rule']

        data = dndApi.getInfo(rule)

        if not data == None:
            if "results" in data:
                data = data["results"]

            options = dndApi.findOptions(data)

            self.displayObject(data, 0)
            

            # this would be a reference back to the same page and can be removed
            if type(data) is dict:
                options.pop(0)

            if len(options) > 0:
                self.main.set_chatOptions(options)


    def displayObject(self, obj, indentLvl):
        if type(obj) is list:
            for index in obj:
                self.displayObject(index, indentLvl)
        
        if type(obj) is dict:
            for key, value in obj.items():
                if not key == 'url' and not key == 'index':
                    self.text.bindObj(ttk.Label(self.text.scrollable_frame, text = indentLvl * "  " + key + ":", 
                        wraplength = self.text.canvas.winfo_width()))
                    self.displayObject(value, indentLvl + 1)
        
        if type(obj) in (str, int, float):
            self.text.bindObj(ttk.Label(self.text.scrollable_frame, text = indentLvl * "  " + str(obj), wraplength = self.text.canvas.winfo_width()))

# the window for the initiative row--------------------------------------------

class initiativeWindow(ttk.Frame):

    def __init__(self,ref main, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.grid(row=0, column=1, rowspan=2)
        self.initiative = list()

        # set user commands
        self.main.addChatCommandGroup("initiative")
        self.main.addChatCommand("initiative", "start", self.start, isPossible = [self.hasCreatures])
        self.main.addChatCommand("initiative", "addcreature", self.AddCreature, parameters = [("name", []), ("initiative", [])])
        self.main.addChatCommand("initiative", "addcreatures", self.AddCreatures, parameters = [("name", []), ("amount", []), ("bonus", [])])
        self.main.addChatCommand("initiative", "removecreature", self.RemoveCreature, parameters = [("name", self.getNames)], isPossible=[self.hasCreatures])
        self.main.addChatCommand("initiative", "nextturn", self.nextTurn, isPossible = [self.nextTurnPossible])

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

# main window ------------------------------------------------------------------

class main(tk.Tk):

    def __init__(self, name, title, server, textCallBack, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.wm_title(title)
        self.sendMsg = textCallBack

        self.videos = videosWindow(ref self, self, server, 2)
        self.text = textWindow(ref self, self, textCallBack)

    def start(self):
        self.mainloop()

    # chat window functions--------------------------------------

    def handleMsg(self, message):
        self.text.chat.handleMsg(message)

    def set_chatOptions(self, options):
        self.text.chat.input.set_options(options)

    # chat commands---------------------------------------------

    def addChatCommandGroup(self, name):
        self.text.commands[name] = commandGroup(name)

    def addChatCommand(self, group, name, callBack, parameters = None, isPossible = None):
        self.text.commands[name].addCommand(name, callBack, parameters, isPossible)

    def testStringWithCommands(self, string):
        for cmdGroup in self.text.commands.values():
            cmdGroup.checkString(string)

    def getCommandOptions(self, data):
        options = list()
        for cmdGroup in self.text.commands.values():
            options += cmdGroup.getOptions(data)

        return options

    # rule window functions------------------------------------

    def displayRule(self, rule):
        self.text.rules.displayRule(rule)

    # initiative window funtions--------------------------------

    def appendInitiativeChanges(self, initiative, curCreature):
        self.text.initiative.appendChanges(initiative, curCreature)