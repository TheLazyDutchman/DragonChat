from dataclasses import dataclass
from enum import Enum

class size(Enum):
    Small = 0
    Medium = 1

def getSize(string):
    print(string)
    return size.Medium

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

def getAlignment(string):
    print(string)
    return alignment.TN

@dataclass
class speed:
    value: int

@dataclass
class walk(speed):
    value: int

def getSpeed(data):
    speeds = list()
    if 'walk' in data:
        speeds.append(walk(int(data['walk'][:-4])))

    return speeds


@dataclass
class abilities:
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int


@dataclass
class sense:
    value: int

@dataclass
class passivePerception(sense):
    value: int

def getSenses(data):
    senses = list()
    if 'passive_perception' in data:
        senses.append(passivePerception(data['passive_perception']))
    
    return senses


@dataclass
class action:
    name: str