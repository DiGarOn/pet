from Plug import Plug
import random

class PlugBoard:
    def __init__(self, number: int, is_random: bool):
        self.number = number
        if number > 13:
            print("it can\'t be more that 13(")
            exit(-1)
        self.plugs = []
        if is_random:
            self.randomisePlugs()
        else:
            self.handlePlugs()

    def randomisePlugs(self):
        chosen = []
        for i in range(self.number):
            rand1 = random.randint(0, 26)
            while rand1 in chosen:
                rand1 = random.randint(0, 26)
            chosen.append(rand1)
            rand2 = random.randint(0, 26)
            while rand2 in chosen:
                rand2 = random.randint(0, 26)
            chosen.append(rand2)
            self.plugs.append(Plug(rand1, rand2))

    def handlePlugs(self, plugs: dict):
        check = set()
        for i in plugs:
            check.union({i, plugs[i]})
        if len(check) != 2 * len(plugs.keys()):
            print("Incorrect plugs. Make another")
            exit(-1)

        for i in plugs:
            self.plugs.append(Plug(i, plugs[i]))

    def runThrough(self, input: int):
        for plug in self.plugs:
            if plug.connect1 == input:
                return plug.connect2
            if plug.connect2 == input:
                return plug.connect1
        return input
