from dataclasses import dataclass
from APIclasses.data import armorclass, category_range, damage, price, fighting_range, weapon_properties, weapon_range, speed

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


@dataclass
class tool(item):
    tool_category: str


@dataclass
class vehicle(item):
    vehicle_category: str

@dataclass
class mount(vehicle):
    speed: speed
    capacity: int

@dataclass
class ship(vehicle):
    speed: speed


@dataclass
class weapon(item):
    weapon_category: str
    weapon_range: weapon_range
    category_range: category_range
    damage: damage
    range: fighting_range
    properties: list[weapon_properties]