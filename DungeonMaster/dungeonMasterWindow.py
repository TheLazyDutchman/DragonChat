import tkinter.ttk as ttk

from pyzmqServer.client import Client

class DungeonMasterWindow(ttk.Frame):
    
    def __init__(self, container, connection: Client) -> None:
        super().__init__(container)
        self.connection = connection

        self.connection.addRequestType("set dungeonMaster")
        self.connection.setRequestHandler("set dungeonMaster", self.start)

    def start(self, event):
        print(event)
        print("started as dungeon master")