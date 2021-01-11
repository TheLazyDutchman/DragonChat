class commandGroup:
    
    def __init__(self, name):
        self.name = name
        self.commands = list()

    def addCommand(self, name, callBack, parameters = None, isPossible = None):
        cmd = command(name, callBack, parameters, isPossible)
        self.commands.append(cmd)

    def checkString(self, test):
        parts = test.split(" ")
        
        if not self.name == parts[0]:
            return

        string = " ".join(parts[1:])

        for cmd in self.commands:
            cmd.checkString(string)

    def getOptions(self, test):
        options = list()
        parts = test.split(" ")

        if parts[0] in self.name:
            options.append((self.name, f"!{self.name}", False))

        if not parts[0] in self.name:
            for cmd in self.commands:

                opt = cmd.getOptions(parts)
                for o in opt:
                    options.append((o[0], f"!{self.name} {o[0]}", o[1]))
        
        if parts[0] == self.name or len(parts[0]) == 0:
            if len(parts) == 1:
                nextParts = [""]
            else:
                nextParts = parts[1:]

            for cmd in self.commands:
                opt = cmd.getOptions(nextParts)
                for o in opt:
                    cmd = f"!{self.name} {o[0]}"
                    run = o[1]

                    if not run:
                        cmd += " "

                    options.append((o[0], cmd, run))

        return options

class command:

    def __init__(self, name, callBack, parameters, isPossible):
        '''
        creates a command, which can be run in the application chat

        Parameters:
            name (str): the name of the command, and what needs to be typed in the chat to run it.
            callBack (callBack): the function to run when the command is called.
            parameters (tupel): the parameters to be extracted from the command call and passed into the callBack
            isPossible ([callBack]): checks to be performed when the getOptions function is called
        '''
        self.name = name
        self.callBack = callBack
        self.parameters = parameters
        self.isPossible = isPossible

    def checkString(self, string):
        parts = string.split(" ")

        params = list()
        if not self.parameters == None:
            if not len(self.parameters) == len(parts[1:]):
                return

        if not self.name == parts[0]:
            return

        if self.parameters == None:
            self.callBack()
        
        for argument in parts[1:]:
            params.append(argument)

        self.callBack(*params)

    def getOptions(self, parts):
        if not parts[0] in self.name:
            return []

        if parts[0] == self.name:
            if self.parameters == None:
                return []

            index = len(parts) - 2
            param = self.parameters[index]

            run = len(self.parameters) > index + 1

            test = parts[-1]

            if type(param[1]) == list:

                return [(f"{' '.join(parts[:-2])} {x}", run) for x in param[1] if test in x]
            
            # else param[1] is a callback, returning a list
            return [(f"{' '.join(parts[:-2])} {x}", run) for x in param[1]() if test in x]

        possible = True
        run = self.parameters == None

        if not self.isPossible == None:
            for check in self.isPossible:
                if not check():
                    possible = False
                    break
            
        return [(self.name, run)] if possible else []
