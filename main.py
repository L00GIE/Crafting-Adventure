import sys
sys.dont_write_bytecode = True

from lib.core import Core
import pygame

pygame.init()
screen = pygame.display.set_mode((1366, 768))
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

pygame.quit()
sys.exit(0)
