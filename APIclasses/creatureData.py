from dataclasses import dataclass

@dataclass
class speed:
    value: int

@dataclass
class walk(speed):
    value: int
@dataclass
class swim(speed):
    value: int
@dataclass
class fly(speed):
    value: int
@dataclass
class climb(speed):
    value: int

def getSpeed(data):
    speeds = list()
    if 'walk' in data:
        speeds.append(walk(int(data['walk'][:-4])))
    if 'swim' in data:
        speeds.append(swim(int(data['swim'][:-4])))
    if 'fly' in data:
        speeds.append(fly(int(data['fly'][:-4])))
    if 'climb' in data:
        speeds.append(climb(int(data['climb'][:-4])))

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