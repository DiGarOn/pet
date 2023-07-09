from Rotor import Rotor
from EndPoint import EndPoint
from PlugBoard import PlugBoard


class Enigma:
    def __init__(self, first: int, second: int, third: int):
        self.rotor1 = Rotor(first, 1)
        self.rotor2 = Rotor(second, 2)
        self.rotor3 = Rotor(third, 3)
        self.end = EndPoint()
        self.plug_board = PlugBoard(10, True)

    def move_rotors(self):
        self.rotor1.position += 1
        if self.rotor1.position == 26:
            self.rotor1.position = 0
            self.rotor2.position += 1
            if self.rotor2.position == 26:
                self.rotor2.position = 0
                self.rotor3.position += 1
                if self.rotor3.position == 26:
                    self.rotor3.position = 0

    def runMachine(self, input: int):
        current_no = self.plug_board.runThrough(input)
        current_no = self.rotor1.runThrough(current_no, True)
        current_no = self.rotor2.runThrough(current_no, True)
        current_no = self.rotor3.runThrough(current_no, True)
        current_no = self.end.runThrough(current_no, True)
        current_no = self.rotor3.runThrough(current_no, False)
        current_no = self.rotor2.runThrough(current_no, False)
        current_no = self.rotor1.runThrough(current_no, False)
        current_no = self.plug_board.runThrough(current_no)

        self.move_rotors()
        return current_no
