from dataclasses import dataclass
from APIclasses.creatureData import size, alignment, speed, abilities, sense, action
import math

@dataclass
class creature:
    name: str
    size: size
    alignment: alignment
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

@dataclass
class monster(creature):
    type: str
    subtype: str
    cr: float
    xp: int
