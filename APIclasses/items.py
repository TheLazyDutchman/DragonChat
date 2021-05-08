from dataclasses import dataclass
from APIclasses.itemData import armorclass, category_range, damage, price, fighting_range, weapon_properties, weapon_range, speed
import tkinter as tk
import tkinter.ttk as ttk

@dataclass
class item:
    name: str
    equipment_category: str
    cost: price
    weight: int
    description: str

    def show(self, window):
        frame = ttk.Frame(window)

        ttk.Label(frame, text=f"Name: {self.name}").pack(anchor="nw")
        ttk.Label(frame, text=f"Category: {self.equipment_category}").pack(anchor="nw")
        self.showCost(frame)

        if self.weight != '':
            ttk.Label(frame, text=f"Weight: {self.weight}").pack(anchor="nw")
            
        if self.description != '':
            ttk.Label(frame, text="Description:").pack(anchor="nw")
            ttk.Label(frame, text=self.description).pack(anchor="nw")

        return frame

    def showCost(self, window):
        ttk.Label(window, text=f"Cost: {self.cost.quantity} {self.cost.unit}").pack(anchor="nw")


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