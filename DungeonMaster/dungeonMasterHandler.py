import tkinter as tk
import tkinter.ttk as ttk

from ServerHandler.Handler import Handler



class DungeonMasterHandler(Handler):

    def startCombat(self):
        self.connection.SendRequest("start combat", [])
