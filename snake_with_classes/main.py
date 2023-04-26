from Window import Window
from Snake import Snake, Food
import pygame


def game_loop(w: Window, f: Food, s: Snake):

    while True:
        w.fill()
        f.draw(w)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        w.update_window()


def main():
    pygame.init()
    w = Window()
    s = Snake(w)
    f = Food(w,s)
    game_loop(w, f, s)


if __name__ == '__main__':
    main()