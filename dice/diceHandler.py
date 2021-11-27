import tkinter as tk

from ServerHandler.Handler import Handler
from DandData.dice import Roll

from .diceFrame import DiceFrame



class DiceHandler(Handler):

    def setMaster(self, master):
        self.master = master
    
    def handleRoll(self, rollName: str, rolls: dict[str, Roll]):
        result: dict[str, int] = {}

        window = tk.Toplevel(master=self.master)
        window.title("Roll dice")

        frames: dict[str, DiceFrame] = {}

        def addResult(name: str, value: int) -> None:
            result[name] = value
            frames[name].pack_forget()

            print(result)
            if len(result) == len(frames):
                
                data = (self.groupName, self.userName, rollName, result)
                answer = self.connection.SendRequest("dice result", data)

                if answer[0] == False:
                    print("could not return dice result: '", answer[1], "'")

                window.destroy()

        for name, roll in rolls.items():
            frames[name] = DiceFrame(window, name, roll, addResult)
            frames[name].pack()
