import os
import pygame
pygame.init()


# MAIN CLASS
class Bird:
    # Loading image
    BIRD_IMAGE = pygame.transform.scale2x(pygame.image.load(os.path.join("Images", "bird1.png")))

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = y
        self.image = self.BIRD_IMAGE

    def jump(self):
        self.y -= 6

    def draw(self, win):
        win.blit(self.BIRD_IMAGE, (self.x, self.y))

    def move(self):
        self.y += 2.5

    def dead_bird(self):
        self.y += 20

    def get_mask(self):
        return pygame.mask.from_surface(self.BIRD_IMAGE)
