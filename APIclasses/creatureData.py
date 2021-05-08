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
class dc:
    type: str
    value: int
    success_type: str

def GetDC(data):
    return dc(
        data['dc_type']['name'],
        data['dc_value'],
        data['success_type']
    )

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
class actionOption:
    name: str
    count: int
    type: str

def GetActionOption(data):
    return actionOption(
        data['name'],
        data['count'],
        data['type']
    )

@dataclass
class actionOptions:
    amount: int
    options: list[actionOption]


def GetActionOptions(data):
    amount = data['choose']
    options = [GetActionOption(x) for x in data['from'][0]]

    return actionOptions(
        amount,
        options
    )

@dataclass
class usage:
    type: str
    dice: str
    min_value: int
    times: int

def GetUsage(data):
    dice = None
    if 'dice' in data:
        dice = data['dice']

    min_value = None
    if 'min_value' in data:
        min_value = data['min_value']

    times= None
    if 'times' in data:
        times = data['times']

    return usage(
        data['type'],
        dice,
        min_value,
        times
    )

@dataclass
class action:
    name: str
    desc: str
    attack_bonus: int
    dc: dc
    actionUsage: usage
    actionDamage: list[damage]
    options: actionOptions

def GetAction(data):
    attack_bonus = None
    if 'attack_bonus' in data:
        attack_bonus = data['attack_bonus']
    
    dc = None
    if 'dc' in data:
        dc = GetDC(data['dc'])

    actionUsage = None
    if 'usage' in data:
        actionUsage = GetUsage(data['usage'])

    actionDamage = [GetDamage(x) for x in data['damage']]

    options = None
    if 'options' in data:
        options = GetActionOptions(data['options'])

    return action(
        data['name'],
        data['desc'],
        attack_bonus,
        dc,
        actionUsage,
        actionDamage,
        options
    )

@dataclass
class legendaryAction:
    name: str
    desc: str

def GetLegendaryAction(data):
    return legendaryAction(
        data['name'],
        data['desc']
    )

@dataclass
class specialAbility:
    name: str
    desc: str
    abilityUsage: usage

def GetSpecialAbility(data):
    abilityUsage = None
    if 'usage' in data:
        abilityUsage = GetUsage(data['usage'])

    return specialAbility(
        data['name'],
        data['desc'],
        abilityUsage
    )
