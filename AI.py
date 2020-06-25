import random
import os
import neat
import visualize
from Bird import Bird
from Pipe import Pipe
from Score import Score

import pygame
pygame.init()


# VARIABLES
WIN_WIDTH = 550
WIN_HEIGHT = 800
GENERATION = 0

# Initializing screen
bg = pygame.transform.scale2x(pygame.image.load("D:/Code/Tensor/Neural Network/Flappy Bird/Images/bg.png"))


# Draw window
def draw_window(win, birds, pipes, s, gen):
    win.blit(bg, (0, 0))
    for pipe in pipes:
        pipe.draw(win)


    s.display_score(win)
    s.show_generation(gen, win)

    for bird in birds:
        bird.draw(win)

    pygame.display.update()

    
# Main function
def main(genomes, config):
    global GENERATION
    GENERATION += 1

    nets, ge, birds = [], [], []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(230, 350))
        g.fitness = 0
        ge.append(g)

    pipes = [Pipe(550)]
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    clock = pygame.time.Clock()

    s = Score()

    score = 0

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 0 and pipes[0].cleared_pipe(birds[0]):
                pipe_ind += 1
        else:
            run = False
            break

        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.15

            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

            if output[0] > 0.5:
                bird.jump()

        add_pipe, previous_pipe = [], []
        for pipe in pipes:
            for x,bird in enumerate(birds):
                if pipe.collision(bird):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)

                if not pipe.passed and pipe.x < bird.x:
                    pipe.passed = True
                    add_pipe = True
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                previous_pipe.append(pipe)

            pipe.move()

        if add_pipe:
            s.update_score()

            for g in ge:
                g.fitness += 3
            pipes.append(Pipe(550))

        for pp in previous_pipe:
            pipes.remove(pp)


        for x, bird in enumerate(birds):
            if bird.y + bird.image.get_height() >= 730 or bird.y < 0:
                birds.pop(x)
                ge.pop(x)
                nets.pop(x)

        # If score exceeds 50, close the game
        if s.count > 50:
            run = False
            break

        draw_window(win, birds, pipes, s, GENERATION)


def run(config_path):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 50)

    # Print out details of best AI
    print("BEST : ", winner)

    # Visualize network
    visualize.draw_net(config, winner, view= True, filename="Network", show_disabled=False, prune_unused=False)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)

    config_path = os.path.join(local_dir, "config-feedforward.txt")

    run(config_path)
