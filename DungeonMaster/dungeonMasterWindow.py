import tkinter.ttk as ttk

from pyzmqServer.client import Client
from .dungeonMasterHandler import DungeonMasterHandler

class DungeonMasterWindow(ttk.Frame):
    
    def __init__(self, container, connection: Client) -> None:
        super().__init__(container)
        self.connection = connection

        self.connection.addRequestType("set dungeonMaster")
        self.connection.setRequestHandler("set dungeonMaster", self.start)

    def start(self, _):
        self.handler = DungeonMasterHandler(self.connection)

        self.startCombatButton = ttk.Button(self, text = "Start Combat", command = self.handler.startCombat)
        self.startCombatButton.pack()