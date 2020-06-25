import pygame
pygame.init()


# Main class
class Score():

    def __init__(self):
        self.count = 0
        self.font = pygame.font.Font("CHICKEN Pie.ttf", 32)
        self.text_x, self.text_y = 10, 10
        self.gen_x, self.gen_y = 400, 10


    def display_score(self, win):
        self.class_score = self.font.render("SCORE : " + str(self.count), True, (255, 0, 0))
        win.blit(self.class_score, (self.text_x, self.text_y))

    def update_score(self):
        self.count += 1

    # Show generation number/counter
    def show_generation(self, generation, win):
        self.generation_counter = self.font.render("GEN : " + str(generation), True, (255, 0, 0))
        win.blit(self.generation_counter, (self.gen_x, self.gen_y))
