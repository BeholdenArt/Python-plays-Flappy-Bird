import random
import os

import pygame
pygame.init()

# Main class
class Pipe():
    # Loading image
    PIPE_BOTTOM = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "pipe.png")))
    PIPE_TOP = pygame.transform.flip(PIPE_BOTTOM, False, True)
    # Pipe pair gap
    GAP = 0
    # Pipe velocity
    PIPE_VELOCITY = 2.5

    def __init__(self, x):
        self.height = 0
        self.x = x
        self.passed = False

        # Top and bottom pipe position
        self.top, self.bottom = 0, 0
        self.pipepair()


    def pipepair(self):
        self.GAP = random.randint(80, 200)
        self.height = random.randint(100, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP


    def cleared_pipe(self, bird):
        if bird.x > self.PIPE_TOP.get_width() + self.x:
            return True
        else:
            return False

    def move(self):
        self.x -= self.PIPE_VELOCITY


    def collision(self, bird):
            bird_mask = bird.get_mask()
            top_mask = pygame.mask.from_surface(self.PIPE_TOP)
            bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)

            top_offset = (round(self.x - bird.x), round(self.top - round(bird.y)))
            bottom_offset = (round(self.x - bird.x), round(self.bottom - round(bird.y)))

            b_point = bird_mask.overlap(bottom_mask, bottom_offset)
            t_point = bird_mask.overlap(top_mask, top_offset)

            if t_point or b_point:
                return True

            return False



    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
