import tkinter as tk
import tkinter.ttk as ttk
from typing import Iterable
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
        if type(rule) == list:
            rule = " ".join(rule)

        self.text.clearFrame()

        data = dndApi.getInfo(rule)

        if not data == None:
            if "results" in data:
                data = data["results"]

            # options = dndApi.findOptions(data)

            self.displayObject(data)            

            # # this would be a reference back to the same page and can be removed
            # if type(data) is dict:
            #     options.pop(0)

            # if len(options) > 0:
            #     self.main.set_chatOptions(options)


    def displayObject(self, obj, indentLevel = 0, url = None):
        if type(obj) in (str, int, float):
            if url == None:
                label = ttk.Label(self.text.scrollable_frame, text = str(obj), wraplength = self.text.canvas.winfo_width())

            else:
                label = ttk.Button(self.text.scrollable_frame, text = str(obj), command=lambda : self.displayRule(url))
            self.text.bindObj(label, indentLevel)

            return label

        if type(obj) == list:
            for data in obj:
                self.displayObject(data, indentLevel = indentLevel)

        if type(obj) == dict:
            toBeDisplayed = list()
            for key, value in obj.items():
                if type(value) == str:
                    if value.startswith("/api/"):
                        if key == "url":
                            toBeDisplayed = toBeDisplayed[3:]
                            toBeDisplayed[0] = [(toBeDisplayed[0][0], value[5:]), toBeDisplayed[0][1]]

                        else:
                            toBeDisplayed.append([(key, value[5:]), indentLevel])

                        continue
                
                if key == "choose":
                    toBeDisplayed.append([f"{key} {value} from:", indentLevel])
                    toBeDisplayed.append([obj["from"], indentLevel + 1])
                    break

                if key == "equipment":
                    toBeDisplayed.append([value, indentLevel])
                    toBeDisplayed.append([f"quantity {obj['quantity']}", indentLevel])
                    break

                toBeDisplayed.append([key + ":", indentLevel])
                toBeDisplayed.append([value, indentLevel + 1])

            for o in toBeDisplayed:
                if type(o[0]) == tuple:
                    self.displayObject(o[0][0], indentLevel=o[1], url = o[0][1])

                self.displayObject(o[0], indentLevel=o[1])

