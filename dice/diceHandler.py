import tkinter as tk
from uuid import UUID

from ServerHandler.Handler import Handler
from DandData.dice import Roll

from .diceFrame import DiceFrame



class DiceHandler(Handler):

    def setMaster(self, master):
        self.master = master
    
    def handleRoll(self, data: tuple[str, UUID, str, dict[str, Roll]]):
        creatureName, creatureId, rollName, rolls = data
        result: dict[str, int] = {}

        window = tk.Toplevel(master=self.master)
        window.title(f"Roll dice for {creatureName}, {rollName}")

        frames: dict[str, DiceFrame] = {}

        def addResult(name: str, value: int) -> None:
            result[name] = value
            frames[name].pack_forget()

            if len(result) == len(frames):
                
                data = (self.groupName, self.userName, creatureId, rollName, result)
                answer = self.connection.SendRequest("dice result", data)

                if answer[0] == False:
                    print("could not return dice result: '", answer[1], "'")

                window.destroy()

        for name, roll in rolls.items():
            frames[name] = DiceFrame(window, name, roll, addResult)
            frames[name].pack()
