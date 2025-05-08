import pygame
import math

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.radius = 20
        self.mouth_opening = True
        self.mouth_angle = 45  
        self.mouth_change_rate = 2  

    def update_position(self, direction):
        self.x += direction[0] * self.speed
        self.y += direction[1] * self.speed

    def draw(self, screen):
        # pacman mounth - eating state
        if self.mouth_opening:
            self.mouth_angle += self.mouth_change_rate
            if self.mouth_angle >= 45:
                self.mouth_opening = False
        else:
            self.mouth_angle -= self.mouth_change_rate
            if self.mouth_angle <= 5:
                self.mouth_opening = True

        start_angle = math.radians(self.mouth_angle)
        end_angle = math.radians(360 - self.mouth_angle)

        pygame.draw.pie(screen, (255, 255, 0), (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2), start_angle, end_angle)

        font = pygame.font.SysFont(None, 24)
        text = font.render("Pacman", True, (255, 255, 255))
        screen.blit(text, (self.x - 30, self.y - 40))
