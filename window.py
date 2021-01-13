import tkinter as tk
import tkinter.ttk as ttk
from cv2 import cv2
from PIL import Image, ImageTk
from chatUI import chatWindow
from rulesUI import rulesWindow
from initiativeUI import initiativeWindow

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

    def __init__(self, main, parent, pos, *args, **kwargs):
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

    def __init__(self, main, parent, server, maxWidth, *args, **kwargs):
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

    def __init__(self, main, parent, chatSendCallback, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main
        self.commands = dict()

        self.grid(row=0, column=1)

        self.chat = chatWindow(self.main, self, chatSendCallback)
        self.rules = rulesWindow(self.main, self)
        self.initiative = initiativeWindow(self.main, self)

# main window ------------------------------------------------------------------

class main(tk.Tk):

    def __init__(self, name, title, server, textCallBack, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.wm_title(title)
        self.sendMsg = textCallBack

        self.videos = videosWindow(self, self, server, 2)
        self.text = textWindow(self, self, textCallBack)

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