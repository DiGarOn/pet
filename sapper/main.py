from tkinter import *
import tkinter.ttk as ttk
import random
from functools import partial


class MainWindow:
    def __init__(self):
        self.window = Tk()

        self.bombs_number = 10

        self.window.title("supper")
        self.window.geometry('500x500')

        self.lbl1 = Label(self.window, text="Choose size")
        self.lbl1.grid(column=0, row=0)

        self.combo = ttk.Combobox(self.window, state='readonly')
        self.combo['values'] = ('8x8', '10x10', '12x12', '16x16', '24x24', '32x32')
        self.combo.current(0)
        self.combo.grid(column=1, row=0)

        self.button = Button(self.window, text='start the game', command=self.Start)
        self.button.grid(column=2, row=0)

        self.data = []

        self.buttoms = []

    def open_1(self, i, j):
        # exit
        if i < 0 or i == len(self.data) or j < 0 or j == len(self.data):
            return
        elif self.buttoms[i][j].cget('text') == self.data[i][j]:
            return
        elif self.data[i][j] > 0:
            self.buttoms[i][j].configure(text=self.data[i][j])
            return
        else:
            self.buttoms[i][j].configure(text=self.data[i][j])
            self.open_1(i + 1, j)
            self.open_1(i, j + 1)
            self.open_1(i - 1, j)
            self.open_1(i, j - 1)

    def pushed(self, i, j):
        if self.data[i][j] == -1:
            end_game_window = Toplevel(self.window)
            lbl = Label(end_game_window, text="Game Over.").pack()
            self.buttoms[i][j].configure(text=self.data[i][j])
        else:
            self.open_1(i, j)

    def Start(self):
        self.buttoms = []
        game_window = Toplevel(self.window)
        size = self.combo.get()
        size = int(size[:size.find('x')])
        self.fullfill_data(size)
        for i in range(size):
            tmp = []
            for j in range(size):
                btn = Button(game_window, height=1, width=2, command=partial(self.pushed, i, j))
                btn.grid(row=i, column=j)
                tmp.append(btn)
            self.buttoms.append(tmp)

        game_window.mainloop()

    def fullfill_data(self, number):
        self.data = []
        tmp_list = []
        for i in range(number):
            for j in range(number):
                tmp_list.append([i, j])
        bombs = random.sample(tmp_list, self.bombs_number)
        for i in range(number):
            tmp = []
            for j in range(number):
                if [i, j] in bombs:
                    tmp.append(-1)
                else:
                    count = 0
                    for k in range(-1, 2, 1):
                        for l in range(-1, 2, 1):
                            if [i+k, j+l] in bombs:
                                count += 1
                    tmp.append(count)

            self.data.append(tmp)

    def run(self):
        self.window.mainloop()


window = MainWindow()
window.run()
