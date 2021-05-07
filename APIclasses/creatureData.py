from APIclasses.itemData import GetDamage, damage
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

def GetSpeed(data):
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

def GetSenses(data):
    senses = list()
    if 'passive_perception' in data:
        senses.append(passivePerception(data['passive_perception']))
    
    return senses

@dataclass
class proficiency:
    name: str
    value: int

def GetProficiency(data):
    return proficiency(
        data['proficiency']['name'],
        data['value']
    )

@dataclass
class action:
    name: str
    desc: str
    attack_bonus: int
    damage: list[damage]

def GetAction(data):
    if "attack_bonus" in data:
        return action(
            data['name'],
            data['desc'],
            data['attack_bonus'],
            [GetDamage(x) for x in data['damage']]
        )

    return "undefined"