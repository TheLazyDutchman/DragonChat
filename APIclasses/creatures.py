from dataclasses import dataclass
from APIclasses.creatureData import GetAction, GetProficiency, GetSenses, GetSpeed, climb, fly, proficiency, speed, swim, walk, abilities, sense, action
import math
import tkinter.ttk as ttk

@dataclass
class creature:
    name: str
    size: str
    alignment: str
    base_ac: int
    base_hp: int
    hp: int
    hit_dice: str
    speed: list[speed]
    abilities: abilities
    proficiencies: list[proficiency]
    dmg_vulnerabilities: list
    dmg_resistances: list
    dmg_immunities: list
    condition_immunities: list
    senses: list[sense]
    languages: list[str]
    actions: list[action]
    reactions: list[action]
    desc: str

    def getSTRbonus(self):
        return math.floor((self.abilities.strength - 10)/2.0)

    def getDEXbonus(self):
        return math.floor((self.abilities.dexterity - 10)/2.0)
    
    def getCONbonus(self):
        return math.floor((self.abilities.constitution - 10)/2.0)

    def getINTbonus(self):
        return math.floor((self.abilities.intelligence - 10)/2.0)

    def getWISbonus(self):
        return math.floor((self.abilities.wisdom - 10)/2.0)

    def getCHAbonus(self):
        return math.floor((self.abilities.charisma - 10)/2.0)

    def getAC(self):
        return self.base_ac

    def show(self, window):
        frame = ttk.Frame(window)

        ttk.Label(frame, text=f"Name: {self.name}").pack(anchor="nw")
        ttk.Label(frame, text=f"Size: {self.size}").pack(anchor="nw")
        ttk.Label(frame, text=f"Alignment: {self.alignment}").pack(anchor="nw")
        ttk.Label(frame, text=f"AC: {self.getAC()}").pack(anchor="nw")
        ttk.Label(frame, text=f"HP: {self.hp}").pack(anchor="nw")
        ttk.Label(frame, text=f"Hit Dice: {self.hit_dice}").pack(anchor="nw")
        self.showSpeed(frame)
        ttk.Label(frame, text=f"STR: {self.getSTRbonus()} ({self.abilities.strength})").pack(anchor="nw")
        ttk.Label(frame, text=f"DEX: {self.getDEXbonus()} ({self.abilities.dexterity})").pack(anchor="nw")
        ttk.Label(frame, text=f"CON: {self.getCONbonus()} ({self.abilities.constitution})").pack(anchor="nw")
        ttk.Label(frame, text=f"INT: {self.getINTbonus()} ({self.abilities.intelligence})").pack(anchor="nw")
        ttk.Label(frame, text=f"WIS: {self.getWISbonus()} ({self.abilities.wisdom})").pack(anchor="nw")
        ttk.Label(frame, text=f"CHA: {self.getCHAbonus()} ({self.abilities.charisma})").pack(anchor="nw")
        self.showProficiencies(frame)
        self.showDmg_vulnerabilities(frame)
        self.showDmg_resistances(frame)
        self.showDmg_immunities(frame)
        self.showLanguages(frame)
        self.showActions(frame)
        self.showReactions(frame)

        return frame

    def showSpeed(self, window):
        for s in self.speed:
            if isinstance(s, walk):
                ttk.Label(window, text=f"walk speed: {s.value}").pack(anchor="nw")
            if isinstance(s, swim):
                ttk.Label(window, text=f"swim speed: {s.value}").pack(anchor="nw")
            if isinstance(s, climb):
                ttk.Label(window, text=f"climb speed: {s.value}").pack(anchor="nw")
            if isinstance(s, fly):
                ttk.Label(window, text=f"fly speed: {s.value}").pack(anchor="nw")

    def showProficiencies(self, window):
        if len(self.proficiencies) == 0:
            return
        ttk.Label(window, text="proficiencies:").pack(anchor="nw")
        for proficiency in self.proficiencies:
            ttk.Label(window, text=proficiency.name + f" ({proficiency.value})").pack(anchor="nw")

    def showLanguages(self, window):
        if len(self.languages) == 0:
            return
        ttk.Label(window, text="languages:").pack(anchor="nw")

        if isinstance(self.languages, list):
            for language in self.languages:
                ttk.Label(window, text=language).pack(anchor="nw")
            return
        ttk.Label(window, text=self.languages).pack(anchor="nw")

    def showActions(self, window):
        if len(self.actions) == 0:
            return
        ttk.Label(window, text="actions:").pack(anchor="nw")
        for action in self.actions:

            if action == "undefined":
                ttk.Label(window, text="action undefined").pack(anchor="nw")
                continue

            ttk.Label(window, text=f"name: {action.name}").pack(anchor="nw")
            ttk.Label(window, text="description:").pack(anchor="nw")
            ttk.Label(window, text=action.desc).pack(anchor="nw")
            ttk.Label(window, text=f"attack bonus: {action.attack_bonus}").pack(anchor="nw")
            ttk.Label(window, text="damage:").pack(anchor="nw")
            for damage in action.damage:
                ttk.Label(window, text=damage.type + f" ({damage.dice})").pack(anchor="nw")


    def showReactions(self, window):
        if len(self.reactions) == 0:
            return
        ttk.Label(window, text="reactions:").pack(anchor="nw")
        for reaction in self.reactions:
            ttk.Label(window, text=reaction).pack(anchor="nw")

    def showDmg_vulnerabilities(self, window):
        if len(self.dmg_vulnerabilities) == 0:
            return
        ttk.Label(window, text="damage vulnerabilities:").pack(anchor="nw")
        for vulnerability in self.dmg_vulnerabilities:
            ttk.Label(window, text=vulnerability).pack(anchor="nw")

    def showDmg_resistances(self, window):
        if len(self.dmg_resistances) == 0:
            return
        ttk.Label(window, text="damage resistances:").pack(anchor="nw")
        for resistance in self.dmg_resistances:
            ttk.Label(window, text=resistance).pack(anchor="nw")

    def showDmg_immunities(self, window):
        if len(self.dmg_immunities) == 0:
            return
        ttk.Label(window, text="damage immunities:").pack(anchor="nw")
        for immunity in self.dmg_immunities:
            ttk.Label(window, text=immunity).pack(anchor="nw")

    def showCondition_immunities(self, window):
        if len(self.condition_immunities) == 0:
            return
        ttk.Label(window, text="condition immunities:").pack(anchor="nw")
        for immunity in self.condition_immunities:
            ttk.Label(window, text=immunity).pack(anchor="nw")

@dataclass
class monster(creature):
    monster_type: str
    subtype: str
    cr: float
    xp: int

    def show(self, window):
        frame = super().show(window)

        ttk.Label(frame, text=f"monster type: {self.monster_type}").pack(anchor="nw")
        if self.subtype != None:
            ttk.Label(frame, text=f"subtype: {self.subtype}").pack(anchor="nw")
        ttk.Label(frame, text=f"challenge rating: {self.cr}").pack(anchor="nw")
        ttk.Label(frame, text=f"xp: {self.xp}").pack(anchor="nw")

        return frame

def GetMonster(monster_data):
    speed = GetSpeed(monster_data['speed'])
    senses = GetSenses(monster_data['senses'])

    ability_scores = abilities(
        monster_data['strength'],
        monster_data['dexterity'],
        monster_data['constitution'],
        monster_data['intelligence'],
        monster_data['wisdom'],
        monster_data['charisma']
    )

    proficiencies = [GetProficiency(x) for x in monster_data['proficiencies']]

    dmg_vulnerabilities = monster_data['damage_vulnerabilities']
    dmg_resistances = monster_data['damage_resistances']
    dmg_immunities = monster_data['damage_immunities']

    condition_immunities = [x['name'] for x in monster_data['condition_immunities']]


    languages = monster_data['languages']

    actions = [GetAction(x) for x in monster_data['actions']]

    reactions = list()
    if "reactions" in monster_data:
        reactions = monster_data['reactions']

    description = ''
    if "desc" in monster_data:
        description = monster_data['desc']

    return monster(
        monster_data['name'],
        monster_data['size'],
        monster_data['alignment'],
        monster_data['armor_class'],
        monster_data['hit_points'],
        monster_data['hit_points'],
        monster_data['hit_dice'],
        speed,
        ability_scores,
        proficiencies,
        dmg_vulnerabilities,
        dmg_resistances,
        dmg_immunities,
        condition_immunities,
        senses,
        languages,
        actions,
        reactions,
        description,
        monster_data['type'],
        monster_data['subtype'],
        monster_data['challenge_rating'],
        monster_data['xp']
    )
