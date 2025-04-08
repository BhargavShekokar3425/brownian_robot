
import random
import math
import numpy as np
import pygame

class BrownianRobot:
    def __init__(self, arena_size=500):
        self.arena_size = arena_size
        # The ball will start of from the centre of the screen/arena
        self.x = arena_size // 2
        self.y = arena_size // 2

        #This is for initial ranomized angles/direction of motion of the robot
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = 2
        
        pygame.init()
        self.screen = pygame.display.set_mode((arena_size, arena_size))
        pygame.display.set_caption("Brownian Motion Robot")
        self.clock = pygame.time.Clock()

    def move(self):
        
        # mathematics/derivatives of the motion of the robot
        dx = self.speed * math.cos(self.angle)
        dy = self.speed * math.sin(self.angle)
        
        next_x = self.x + dx
        next_y = self.y + dy
        
        # to fix for boundary collision settings
        if (next_x <= 0 or next_x >= self.arena_size or 
            next_y <= 0 or next_y >= self.arena_size):
            
            # This is ranomized in order to ensure truly random motion/not probable to predict where the robot might head itself into
            self.angle = random.uniform(0, 2 * math.pi)
        else:
            self.x = next_x
            self.y = next_y

    def draw(self):
        self.screen.fill((255, 255, 255))
        
        # The arena to be expected an rectangle screen
        pygame.draw.rect(self.screen, (0, 0, 0), 
                        (0, 0, self.arena_size, self.arena_size), 2)
        
        # making of the robot/designing a red dot
        pygame.draw.circle(self.screen, (255, 0, 0), 
                         (int(self.x), int(self.y)), 5)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.move()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
def run_demo():
    robot = BrownianRobot(arena_size=500)
    robot.run()
