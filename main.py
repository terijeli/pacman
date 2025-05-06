import pygame
from ghost import Ghost
from pacman import Pacman

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pacman FSM Ghost AI")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

pacman = Pacman(300, 200)
ghost = Ghost(100, 100, (255, 0, 0))

power_pellet_active = False
power_pellet_timer = 0
running = True

while running:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            power_pellet_active = True
            power_pellet_timer = pygame.time.get_ticks()

    # power pellet deactivation (after 5 sec)
    if power_pellet_active and pygame.time.get_ticks() - power_pellet_timer > 5000:
        power_pellet_active = False

    pacman.move(keys)
    ghost.update_state(pacman.rect.center, power_pellet_active, False)
    ghost.move(pacman.rect.center)

    pacman.draw(screen)
    ghost.draw(screen, font)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
