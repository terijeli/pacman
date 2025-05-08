import pygame
import random
import math

# pygame set up
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man FSM Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# pacman class
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 4
        self.radius = 20
        self.direction = (1, 0)
        self.mouth_open = True
        self.angle = 45

    def update(self, keys):
        dx, dy = 0, 0
        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1
        elif keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1

        if dx or dy:
            self.direction = (dx, dy)
            self.x += dx * self.speed
            self.y += dy * self.speed

        # pacman eating mode
        self.angle += 3 if self.mouth_open else -3
        if self.angle >= 45:
            self.mouth_open = False
        elif self.angle <= 5:
            self.mouth_open = True

    def draw(self, screen):
        start_angle = math.radians(self.angle)
        end_angle = math.radians(360 - self.angle)
        direction_angle = math.atan2(self.direction[1], self.direction[0])

        rotated_start = direction_angle + start_angle
        rotated_end = direction_angle + end_angle

        # mouth (wedge)
        pygame.draw.circle(screen, (255, 255, 0), (int(self.x), int(self.y)), self.radius)
        mouth_point1 = (self.x, self.y)
        mouth_point2 = (self.x + math.cos(rotated_start) * self.radius, self.y + math.sin(rotated_start) * self.radius)
        mouth_point3 = (self.x + math.cos(rotated_end) * self.radius, self.y + math.sin(rotated_end) * self.radius)
        pygame.draw.polygon(screen, (0, 0, 0), [mouth_point1, mouth_point2, mouth_point3])

        text = font.render("Pacman", True, (255, 255, 255))
        screen.blit(text, (self.x - 30, self.y - 40))

# FSM states
class GhostState:
    def update(self, ghost, pacman):
        pass

class ChaseState(GhostState):
    def update(self, ghost, pacman):
        ghost.color = (255, 0, 0)
        dx = pacman.x - ghost.x
        dy = pacman.y - ghost.y
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx /= distance
            dy /= distance
        ghost.x += dx * ghost.speed
        ghost.y += dy * ghost.speed

class ScatterState(GhostState):
    def update(self, ghost, pacman):
        ghost.color = (0, 0, 255)
        corner = (0, 0)
        dx = corner[0] - ghost.x
        dy = corner[1] - ghost.y
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx /= distance
            dy /= distance
        ghost.x += dx * ghost.speed
        ghost.y += dy * ghost.speed

class FrightenedState(GhostState):
    def update(self, ghost, pacman):
        ghost.color = (0, 255, 255)
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx /= distance
            dy /= distance
        ghost.x += dx * ghost.speed
        ghost.y += dy * ghost.speed

# ghost class
class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.speed = 2
        self.state = ChaseState()
        self.timer = 0
        self.color = (255, 0, 0)

    def update(self, pacman):
        self.timer += 1
        if self.timer >= 180:
            self.timer = 0
            if isinstance(self.state, ChaseState):
                self.state = ScatterState()
            elif isinstance(self.state, ScatterState):
                self.state = FrightenedState()
            else:
                self.state = ChaseState()

        self.state.update(self, pacman)

    def draw(self, screen):
        # ghost body
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        # ghost eyes
        eye_offset = 7
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x - eye_offset), int(self.y - 5)), 5)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x + eye_offset), int(self.y - 5)), 5)
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x - eye_offset), int(self.y - 5)), 2)
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x + eye_offset), int(self.y - 5)), 2)

        # label
        label = f"Ghost - {self.state.__class__.__name__}"
        text = font.render(label, True, (255, 255, 255))
        screen.blit(text, (self.x - 50, self.y - 40))

# game loop
pacman = Pacman(100, 100)
ghost = Ghost(400, 300)
running = True

while running:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pacman.update(keys)
    ghost.update(pacman)

    pacman.draw(screen)
    ghost.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
