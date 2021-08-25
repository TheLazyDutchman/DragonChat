import tkinter as tk
import tkinter.ttk as ttk
from Creatures.Actions.Action import Action



class ActionWindow(ttk.Frame):

    def __init__(self, action: Action, master = None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.action = action

        ttk.Label(master = self, text = self.action.name).pack()

        desc = tk.Text(master = self, width = 40, height = 4, wrap='word')
        desc.insert(tk.END, self.action.desc)
        desc.config(state = 'disabled')
        desc.pack()