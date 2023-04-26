from Window import Window
from Snake import Snake
from Food import Food
import pygame


def game_loop(w: Window, f: Food, s: Snake):
    clock = pygame.time.Clock()#
    while True:
        clock.tick(s.speed)  #
        w.fill()
        f.draw(w)
        s.draw(w)
        s.move()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    s.change_direction('left')
                elif event.key == pygame.K_RIGHT:
                    s.change_direction('right')
                elif event.key == pygame.K_UP:
                    s.change_direction('up')
                elif event.key == pygame.K_DOWN:
                    s.change_direction('down')
        w.update_window()
        s.check_eat(f, w)
        if s.check_collapse(w):
            pygame.quit() #
            exit()


def main():
    pygame.init()
    w = Window()
    s = Snake(w)
    f = Food(w,s)
    game_loop(w, f, s)


if __name__ == '__main__':
    main()