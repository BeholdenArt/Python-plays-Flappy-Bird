import pygame
pygame.init()

# Main class
class Score:

    def __init__(self):
        self.count = 0
        self.font = pygame.font.SysFont("Consolas", 32)
        self.score_x, self.score_y = 10, 40
        self.gen_x, self.gen_y = 150, 10
        self.pop_x, self.pop_y = 250, 40

    def display_score(self, win):
        class_score = self.font.render("SCORE : " + str(self.count), True, (255, 0, 0))
        win.blit(class_score, (self.score_x, self.score_y))

    def update_score(self):
        self.count += 1

    def display_pop_size(self, window, birds_len):
        pop_size = self.font.render("Population : " + str(birds_len), True, (255, 0, 0))
        window.blit(pop_size, (self.pop_x, self.pop_y))
        pass

    # Show generation number/counter
    def show_generation(self, generation, win):
        generation_counter = self.font.render("GEN : " + str(generation), True, (255, 0, 0))
        win.blit(generation_counter, (self.gen_x, self.gen_y))
