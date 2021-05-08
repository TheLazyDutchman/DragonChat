from dataclasses import dataclass
from enum import Enum

class currency(Enum):
    copper = 0
    silver = 1
    electrum = 2
    gold = 3
    platinum = 4

def getCurrency(string):
    print(string)
    return currency.gold

class weapon_range(Enum):
    melee = 0
    ranged = 1

class category_range(Enum):
    martial_melee = 0
    martial_ranged = 1
    simple_melee = 2
    simple_ranged = 3

@dataclass
class price:
    quantity: int
    unit: currency

@dataclass
class armorclass:
    base: int
    dex_bonus: bool
    max_bonus: int

@dataclass
class damage:
    dice: str
    type: str

def GetDamage(data):
    return damage(
        data['damage_dice'],
        data['damage_type']['name']
    )

@dataclass
class fighting_range:
    normal: int
    long: int

@dataclass
class weapon_properties:
    property: str

@dataclass
class speed:
    quantity: int
    unit: str

@dataclass
class condition:
    name: str
    desc: str

@dataclass
class magic_school:
    name: str
    desc: str