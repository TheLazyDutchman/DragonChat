import tkinter as tk
import tkinter.ttk as ttk
import dndApi
from ScrollableFrame import ScrollableFrame

class rulesWindow(ttk.Frame):
    
    def __init__(self, main, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.main = main
        self.grid(row=1, column=0)

        self.title = ttk.Label(self, text="rules")
        self.title.pack()

        self.text = ScrollableFrame(self)
        self.text.pack()

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
