import sys
sys.dont_write_bytecode = True

from lib.core import Core
import pygame

pygame.init()
screen = pygame.display.set_mode((1366, 768))
loading = pygame.transform.scale(pygame.image.load("data/assets/UI/loading.jpg"), (screen.get_width(), screen.get_height()))
screen.blit(loading, (0, 0))
pygame.display.update()
clock = pygame.time.Clock()
core = Core(screen)
running = True

while running:
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            running = False
    if running:
        core.loop(ev)
        clock.tick(60)
        pygame.display.set_caption(f"Crafting Adventure | {round(clock.get_fps(), 1)}")
        pygame.display.update()

core.save()
pygame.quit()
sys.exit(0)
