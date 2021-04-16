from dataclasses import dataclass
from enum import Enum

class currency(Enum):
    copper = 0
    silver = 1
    electrum = 2
    gold = 3
    platinum = 4

class damage_type(Enum):
    acid = 0
    bludgeoning = 1
    cold = 2
    fire = 3
    force = 4
    lightning = 5
    necrotic = 6
    piercing = 7
    poison = 8
    psychic = 9
    radiant = 10
    slashing = 11
    thunder = 12

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
    type: damage_type

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