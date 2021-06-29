from typing import Callable
from ServerHandler.Handler import Handler

class EventHandler(Handler):

    def __init__(self, groupName: str, userName: str, sendSocket):
        super().__init__(groupName, userName, sendSocket)
        self.listeners: dict[str, Callable] = {}

    def addListener(self, eventType: str, callback: Callable):
        if eventType in self.listeners:
            return "there is already a listener for event " + eventType

        self.listeners[eventType] = callback

    def HandleEvent(self, eventType, data):
        if not eventType in self.listeners:
            return "there is no listener for event " + eventType

        self.listeners[eventType](data)