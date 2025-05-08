import pygame
import math
import random
from states import ChaseState, ScatterState, FrightenedState

class Ghost:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.state = ChaseState()
        self.state_timer = 0
        self.radius = 20
        self.color = (255, 0, 0)

    def update(self, pacman_pos):
        # update state timer
        self.state_timer += 1
        if self.state_timer >= 180:  # state change every 3 seconds
            self.state_timer = 0
            if isinstance(self.state, ChaseState):
                self.state = ScatterState()
            elif isinstance(self.state, ScatterState):
                self.state = FrightenedState()
            elif isinstance(self.state, FrightenedState):
                self.state = ChaseState()

        # update color based on the state
        if isinstance(self.state, ChaseState):
            self.color = (255, 0, 0)  # Red
        elif isinstance(self.state, ScatterState):
            self.color = (0, 0, 255)  # Blue
        elif isinstance(self.state, FrightenedState):
            self.color = (0, 255, 255)  # Cyan

        # state behavior execution
        self.state.execute(self, pacman_pos)

    def draw(self, screen):
        # draw the ghost body (circle)
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        # draw eyes
        eye_radius = 5
        eye_offset_x = 7
        eye_offset_y = -5
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x - eye_offset_x), int(self.y + eye_offset_y)), eye_radius)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x + eye_offset_x), int(self.y + eye_offset_y)), eye_radius)

        # draw pupils
        pupil_radius = 2
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x - eye_offset_x), int(self.y + eye_offset_y)), pupil_radius)
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x + eye_offset_x), int(self.y + eye_offset_y)), pupil_radius)

        # write "ghost" and its current state
        font = pygame.font.SysFont(None, 24)
        text = font.render(f"Ghost - {self.state.__class__.__name__}", True, (255, 255, 255))
        screen.blit(text, (self.x - 40, self.y - 40))
