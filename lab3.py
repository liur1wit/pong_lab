import pygame
from paddle import Paddle
from ball import Ball
from random import randint
from collections import namedtuple

# define a main function
def main():
    pygame.init()
    pygame.display.set_caption("My Pong")

    WIDTH = 800
    HEIGHT = 480
    BORDER = 20
    VELOCITY = 5
    FPS = 30

    MyConstants = namedtuple("MyConstants",["WIDTH", "HEIGHT", "BORDER", "VELOCITY", "FPS"])

    CONSTS = MyConstants(WIDTH, HEIGHT, BORDER, VELOCITY, FPS)
    
    #surface
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # add a solid background as r,g,b:
    screen.fill((0, 0, 0))
    
    # double buffering: stage updates together; update them at once.
    # avoids flickering.
    pygame.display.update()
    
    # Walls
    # Rect(surface, color, rect) -> Rect
    wcolor = pygame.Color("white")
    
    bcolor = pygame.Color("yellow")

    #upper wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    #left wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    #bottom wall
    pygame.draw.rect(screen, wcolor, pygame.Rect((0,HEIGHT - BORDER), (WIDTH, BORDER)))
    pygame.display.update()

    #Ball init
    x0 = WIDTH - Ball.RADIUS
    y0 = HEIGHT // 2
    vx0 = -VELOCITY
    vy0 = randint(-VELOCITY, VELOCITY)
    b0 = Ball(x0, y0, vx0, vy0, screen, bcolor, pygame.Color("Black"), CONSTS)
    
    b0.show(bcolor)
    pygame.display.update()
    
    # define a variable to control the main loop
    running = True
    clock = pygame.time.Clock()
        
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.display.update()
        clock.tick(FPS)
        # Ball
        b0.update()
        

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()