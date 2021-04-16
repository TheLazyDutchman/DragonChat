from dataclasses import dataclass
from enum import Enum

class size(Enum):
    small = 0
    medium = 1

class alignment(Enum):
    LG = 0
    NG = 1
    CG = 2
    LN = 3
    TN = 4
    CN = 5
    LE = 6
    NE = 7
    CE = 8

@dataclass
class speed: int

@dataclass
class walk(speed): int


@dataclass
class abilities:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


@dataclass
class sense: int

@dataclass
class passivePerception(sense): int


@dataclass
class action:
    name: str