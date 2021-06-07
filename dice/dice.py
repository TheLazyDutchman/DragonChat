import random
import regex

def RollDice(diceString):
    match = regex.search(r"(\d*)d(\d+)([ad]?)(\+(\d+))?", diceString)

    diceAmount = match.groups()[0]
    if diceAmount == '':
        diceAmount = '1'
    diceAmount = int(diceAmount)

    diceType = int(match.groups()[1])

    advantage = (match.groups()[2] == 'a')
    disadvantage = (match.groups()[2] == 'd')

    bonus = match.groups()[4]
    if bonus == None:
        bonus = 0
    bonus = int(bonus)
    
    sum = 0
    for i in range(diceAmount):
        amount = random.randint(1, diceType)
        if not (advantage and disadvantage):
            if advantage:
                amount = max(amount, random.randint(1, diceType))
            if disadvantage:
                amount = min(amount, random.randint(1, diceType))
        sum += amount
    
    return sum + bonus