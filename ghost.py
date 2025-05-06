import pygame
from fsm import GhostState
import random

class Ghost:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.color = color
        self.state = GhostState.SCATTER
        self.speed = 2
        self.base_pos = (x, y)
    
    def update_state(self, pacman_pos, is_power_pellet_active, is_eaten):
        distance = self.get_distance(pacman_pos)
        if is_eaten:
            self.state = GhostState.DEAD
        elif is_power_pellet_active:
            self.state = GhostState.FRIGHTENED
        elif distance < 100:
            self.state = GhostState.CHASE
        else:
            self.state = GhostState.SCATTER

    def get_distance(self, pacman_pos):
        dx = pacman_pos[0] - self.rect.x
        dy = pacman_pos[1] - self.rect.y
        return (dx**2 + dy**2) ** 0.5

    def move(self, pacman_pos):
        if self.state == GhostState.SCATTER:
            self.rect.x += random.choice([-1, 1]) * self.speed
            self.rect.y += random.choice([-1, 1]) * self.speed
        elif self.state == GhostState.CHASE:
            if pacman_pos[0] > self.rect.x:
                self.rect.x += self.speed
            elif pacman_pos[0] < self.rect.x:
                self.rect.x -= self.speed
            if pacman_pos[1] > self.rect.y:
                self.rect.y += self.speed
            elif pacman_pos[1] < self.rect.y:
                self.rect.y -= self.speed
        elif self.state == GhostState.FRIGHTENED:
            self.rect.x += random.choice([-1, 1]) * self.speed
            self.rect.y += random.choice([-1, 1]) * self.speed
        elif self.state == GhostState.DEAD:
            # Go back to base position
            if self.rect.x < self.base_pos[0]:
                self.rect.x += self.speed
            elif self.rect.x > self.base_pos[0]:
                self.rect.x -= self.speed
            if self.rect.y < self.base_pos[1]:
                self.rect.y += self.speed
            elif self.rect.y > self.base_pos[1]:
                self.rect.y -= self.speed

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        state_text = font.render(self.state.name, True, (255, 255, 255))
        screen.blit(state_text, (self.rect.x, self.rect.y - 20))
