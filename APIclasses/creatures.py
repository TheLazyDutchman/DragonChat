from dataclasses import dataclass
from APIclasses.creatureData import climb, fly, speed, swim, walk, abilities, sense, action
import math
import tkinter.ttk as ttk

@dataclass
class creature:
    name: str
    size: str
    alignment: str
    base_ac: int
    base_hp: int
    hp: int
    hit_dice: str
    speed: list[speed]
    abilities: abilities
    proficiencies: list
    dmg_vulnerabilities: list
    dmg_resistances: list
    dmg_immunities: list
    condition_immunities: list
    senses: list[sense]
    language: list[str]
    actions: list[action]
    reactions: list[action]

    def getSTRbonus(self):
        return math.floor((self.abilities.strength - 10)/2.0)

    def getDEXbonus(self):
        return math.floor((self.abilities.dexterity - 10)/2.0)
    
    def getCONbonus(self):
        return math.floor((self.abilities.constitution - 10)/2.0)

    def getINTbonus(self):
        return math.floor((self.abilities.intelligence - 10)/2.0)

    def getWISbonus(self):
        return math.floor((self.abilities.wisdom - 10)/2.0)

    def getCHAbonus(self):
        return math.floor((self.abilities.charisma - 10)/2.0)

    def getAC(self):
        return self.base_ac

    def show(self, window):
        frame = ttk.Frame(window)

        ttk.Label(frame, text=f"Name: {self.name}").pack()
        ttk.Label(frame, text=f"Size: {self.size}").pack()
        ttk.Label(frame, text=f"Alignment: {self.alignment}").pack()
        ttk.Label(frame, text=f"AC: {self.getAC()}").pack()
        ttk.Label(frame, text=f"HP: {self.hp}").pack()
        ttk.Label(frame, text=f"Hit Dice: {self.hit_dice}").pack()
        self.showSpeed(frame)
        ttk.Label(frame, text=f"STR: {self.getSTRbonus()} ({self.abilities.strength})").pack()
        ttk.Label(frame, text=f"DEX: {self.getDEXbonus()} ({self.abilities.dexterity})").pack()
        ttk.Label(frame, text=f"CON: {self.getCONbonus()} ({self.abilities.constitution})").pack()
        ttk.Label(frame, text=f"INT: {self.getINTbonus()} ({self.abilities.intelligence})").pack()
        ttk.Label(frame, text=f"WIS: {self.getWISbonus()} ({self.abilities.wisdom})").pack()
        ttk.Label(frame, text=f"CHA: {self.getCHAbonus()} ({self.abilities.charisma})").pack()

        return frame

    def showSpeed(self, window):
        for s in self.speed:
            if isinstance(s, walk):
                ttk.Label(window, text=f"walk speed: {s.value}").pack()
            if isinstance(s, swim):
                ttk.Label(window, text=f"swim speed: {s.value}").pack()
            if isinstance(s, climb):
                ttk.Label(window, text=f"climb speed: {s.value}").pack()
            if isinstance(s, fly):
                ttk.Label(window, text=f"fly speed: {s.value}").pack()

@dataclass
class monster(creature):
    monster_type: str
    subtype: str
    cr: float
    xp: int

    def show(self, window):
        frame = super().show(window)

        ttk.Label(frame, text=f"monster type: {self.monster_type}").pack()
        ttk.Label(frame, text=f"subtype: {self.subtype}").pack()
        ttk.Label(frame, text=f"challenge rating: {self.cr}").pack()
        ttk.Label(frame, text=f"xp: {self.xp}").pack()

        return frame
