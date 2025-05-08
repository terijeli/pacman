import pygame
import math
import random

class GhostState:
    def execute(self, ghost, pacman_pos):
        pass

class ChaseState(GhostState):
    def execute(self, ghost, pacman_pos):
        # moving to pacman
        dx = pacman_pos[0] - ghost.x
        dy = pacman_pos[1] - ghost.y
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx /= distance
            dy /= distance
        ghost.x += dx * ghost.speed
        ghost.y += dy * ghost.speed

class ScatterState(GhostState):
    def execute(self, ghost, pacman_pos):
        # moving to the upper left corner (0,0)
        dx = 0 - ghost.x
        dy = 0 - ghost.y
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx /= distance
            dy /= distance
        ghost.x += dx * ghost.speed
        ghost.y += dy * ghost.speed

class FrightenedState(GhostState):
    def execute(self, ghost, pacman_pos):
        # random direction move
        dx = random.choice([-1, 0, 1])
        dy = random.choice([-1, 0, 1])
        distance = math.hypot(dx, dy)
        if distance != 0:
            dx /= distance
            dy /= distance
        ghost.x += dx * ghost.speed
        ghost.y += dy * ghost.speed
