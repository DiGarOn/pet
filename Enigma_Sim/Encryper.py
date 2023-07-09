from Enigma import Enigma

class Encrypter:
    def __init__(self, input: str):
        self.input = input
        self.input = self.input.lower()
        self.enigma = Enigma(2, 1, 4)

    def encrypt(self):
        res = ''
        for i in self.input:
            tmp = ord(i) - ord('a')
            tmp = self.enigma.runMachine(tmp)
            res += chr(tmp + ord('a'))
        return res
