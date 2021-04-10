from dataclasses import dataclass
from enum import Enum

class currency(Enum):
    copper = 0
    silver = 1
    electrum = 2
    gold = 3
    platinum = 4

@dataclass
class price:
    quantity: int
    unit: currency

@dataclass
class armorclass:
    base: int
    dex_bonus: bool
    max_bonus: int