import tkinter as tk
import tkinter.ttk as ttk
import time
from ScrollableFrame import ScrollableFrame

class chatTextWindow(ScrollableFrame):

    def __init__(self, main, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.grid(row=0, column=0)

    def displayMessage(self, message):
        self.bindObj(ttk.Label(self.scrollable_frame, text=message))
        time.sleep(0.01)
        self.canvas.yview_moveto(1)

class chatInputWindow(ttk.Frame):

    def __init__(self, main, parent, callBack, *args, **kwargs):
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
                self.callBack(text)
            else:
                self.selectedCommand[1].callCommand(self.parameters)
            
            self.input.delete(0, len(text))

    def set_options(self, options):
        optionsVar = tk.StringVar(value=[x[0] for x in options])
        self.selectedCommand = options[0]
        self.optnListBox = tk.Listbox(self, height = 6, listvariable = optionsVar)
        self.optnListBox.grid(row=1, column=0)
        self.parameters = self.textVar.get().split(" ")[1:]

        def select(event):
            self.selectedCommand = options[self.optnListBox.curselection()[0]]
            self.selectedCommand[1].callCommand(self.parameters)

        self.optnListBox.bind('<<ListboxSelect>>', select)

class chatWindow(ttk.Frame):

    def __init__(self, main, parent, chatHandler, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main

        self.text = chatTextWindow(self.main, self)
        self.input = chatInputWindow(self.main, self, chatHandler.sendMessage)

        self.grid(row=0, column=0, )

    def handleMsg(self, msg):
        self.text.displayMessage(msg)
