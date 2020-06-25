import random
import os
from Bird import Bird
from Pipe import Pipe
from Score import Score

import pygame
pygame.init()

WIN_WIDTH = 550
WIN_HEIGHT = 800


def main():
    b = Bird(230, 350)
    p = Pipe(550)
    s = Score()

    run = True
    while run:

        clock.tick(60)
        win.blit(bg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break




        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            b.jump()

        if p.collision(b):
            b.dead_bird()
            print("SCORE : " +str(s.count))
            break

        if p.cleared_pipe(b):
            p = Pipe(550)
            s.update_score()


        s.display_score(win)
        b.draw(win)
        p.draw(win)
        p.move()
        b.move()
        pygame.display.update()

if __name__ == "__main__":
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    bg = pygame.transform.scale2x(pygame.image.load("D:/Code/Tensor/Neural Network/Flappy Bird/Images/bg.png"))
    clock = pygame.time.Clock()

    main()
