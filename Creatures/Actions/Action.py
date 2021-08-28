from dataclasses import dataclass
from typing import Optional



@dataclass
class Damage:
    damage_type: str
    damage_dice: str

@dataclass
class dc:
    dc_type: str
    dc_value: int
    success_type: str

@dataclass
class Usage:
    type: str

@dataclass
class RechargeUsage(Usage):
    dice: str
    min_value: int

@dataclass
class PerDayUsage(Usage):
    times: int


@dataclass
class Action:
    name: str
    desc: str
    damage: list[Damage]
    usage: Optional[Usage]

@dataclass
class MultiattackOption:
    name: str
    count: int
    type: str

@dataclass
class Multiattack(Action):
    num: int
    options: list[list[MultiattackOption]]

@dataclass
class Attack(Action):
    attack_bonus: int
    dc: Optional[dc] = None

@dataclass
class SaveAttack(Action):
    dc: dc


class DCFactory:

    def Create(self, data: dict) -> dc:
        data["dc_type"] = data["dc_type"]["name"]
        return dc(**data)

class DamageFactory:

    def Create(self, data: dict) -> dc:
        data["damage_type"] = data["damage_type"]["name"]
        return Damage(**data)

class UsageFactory:

    def Create(self, data: dict) -> dc:
        if data["type"] == "recharge on roll":
            return RechargeUsage(**data)
        if data["type"] == "per day":
            return PerDayUsage(**data)

class ActionFactory:
    dcFactory = DCFactory()
    damageFactory = DamageFactory()
    usageFactory = UsageFactory()

    def Create(self, data: dict) -> Action:
        data["damage"] = [self.damageFactory.Create(dmg) for dmg in data["damage"]]
        if "damage_dice" in data:
            data["damage"].append(Damage(damage_type = "", damage_dice = data["damage_dice"]))
            data.pop("damage_dice")

        if "usage" in data:
            data["usage"] = self.usageFactory.Create(data["usage"])
        else:
            data["usage"] = None

        if "dc" in data:
            data["dc"] = self.dcFactory.Create(data["dc"])

        if "options" in data:
            data["num"] = data["options"]["choose"]
            data["options"] = [
                    [MultiattackOption(**option) for option in optionList] 
                    for optionList in data["options"]["from"]
                ]
            return Multiattack(**data)

        if "attack_bonus" in data:
            return Attack(**data)

        return SaveAttack(**data)