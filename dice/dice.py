import random
import regex

def RollDice(diceString):
    # d20 + 6, 4d6 + 2, d20a + 3
    match = regex.search(r"(\d*)d(\d+)([ad]?)(\+(\d+))?", diceString)
    print(match, match.groups())

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

print(RollDice("2d6+4"))
print(RollDice("d20+4"))
print(RollDice("d20a+10"))