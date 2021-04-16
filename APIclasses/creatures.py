from dataclasses import dataclass
from APIclasses.creatureData import size, alignment, speed, abilities, sense, action

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

@dataclass
class monster(creature):
    type: str
    subtype: str
    cr: str
    xp: int
