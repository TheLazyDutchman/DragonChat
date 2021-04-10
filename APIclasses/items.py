from dataclasses import dataclass
from APIclasses.data import armorclass, price

@dataclass
class item:
    name: str
    equipment_category: str
    cost: price
    weight: int
    description: str


@dataclass
class gear(item):
    gear_category: str

@dataclass
class pack(gear):
    contents: list[item]

@dataclass
class ammo(gear):
    quantity: int


@dataclass
class armor(item):
    armor_category: str
    armor_class: armorclass
    str_minimum: int
    stealth_disadvantage: bool