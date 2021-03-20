class Command:

    def __init__(self, name, callBack, argCount = 0, baseValues = [], argOptions = []):
        self.name = name
        self.callBack = callBack
        self.argCount = argCount
        self.baseValues = baseValues
        self.argOptions = argOptions

    def getOptions(self, inp):
        options = []
        userInput = inp.split(" ")
        if userInput[0] in self.name:
            options.append(NewOption(self.name, self))

        return options

    
    def callCommand(self, parameters = []):
        if len(parameters) == 0:
            self.callBack()
        else:
            self.callBack(*[parameters])

def NewOption(name, command):
    return (name, command)

def callBackFuntion(name, string, call = "bonjour", **kwargs):
    i = 0
    for _ in range(10):
        print(i)
    return "hello world!"

# add a command from code
# check from user input if this command must be ran
# get parameters from user input
# from user input, get possible commands and parameters while typing (autocomplete)