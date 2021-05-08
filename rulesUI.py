import tkinter as tk
import tkinter.ttk as ttk
from typing import Iterable
import dndApi
from ScrollableFrame import ScrollableFrame

class rulesWindow(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid(row=1, column=0)

        self.title = ttk.Label(self, text="rules")
        self.title.grid(column=0, row=0)

        self.text = ScrollableFrame(self)
        self.text.grid(column=0, row=1)

        self.searchVar = tk.StringVar()
        self.searchBox = ttk.Entry(self, textvariable=self.searchVar)
        self.searchBox.grid(column=1, row=0)

        self.searchVar.trace('w', lambda *args: self.showOptions(self.searchVar.get()))

        self.searchOptionsBox = ScrollableFrame(self, width=160)
        self.options = []
        self.options.append(('Monsters', dndApi.searchMonster('')['results']))
        self.options.append(('Items', dndApi.searchItem('')['results']))

        self.searchOptionsBox.grid(column=1, row=1)
        self.showOptions('')

    def showOptions(self, name: str):
        self.searchOptionsBox.clearFrame()
        name = name.lower()

        for optionList in self.options:
            label = ttk.Label(self.searchOptionsBox.scrollable_frame, text=optionList[0])
            self.searchOptionsBox.bind(label)
            label.pack()

            for option in optionList[1]:
                if name in option['name'].lower():
                    button = ttk.Button(
                        self.searchOptionsBox.scrollable_frame, 
                        text=option['name'], 
                        command=lambda type=optionList[0], url=option['url']:self.showRule(type, url)
                    )
                    button.pack()
                    self.searchOptionsBox.bind(button) # make scrolling work with mouse over the button

    def showRule(self, type, url):
        self.text.clearFrame()
        
        if type == 'Monsters':
            monster = dndApi.getMonster(url)
            if monster == None:
                return
            frame = monster.show(self.text.scrollable_frame)
            frame.pack()
            self.text.bind(frame)
            for child in frame.winfo_children():
                self.text.bind(child)

        if type == 'Items':
            item = dndApi.getItem(url)
            if item == None:
                return
            frame = item.show(self.text.scrollable_frame)
            frame.pack()
            self.text.bind(frame)
            for child in frame.winfo_children():
                self.text.bind(child)
