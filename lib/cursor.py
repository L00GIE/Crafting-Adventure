import pygame
from lib.collider import Collider

class Cursor:

    def __init__(self, core):
        self.core = core
        self.x = 0
        self.y = 0
        self.w = 1
        self.h = 1
        self.collider = Collider(self, debug=False)
        self.initSprite()
        self.cursor = self.pointer
        pygame.mouse.set_visible(False)

    def loop(self):
        pos = pygame.mouse.get_pos()
        self.x = pos[0]
        self.y = pos[1]
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        self.core.screen.blit(self.cursor, (self.x, self.y))

    def initSprite(self):
        ss = pygame.image.load("data/assets/Tileset/spr_tileset_sunnysideworld_16px.png")
        self.pointer = ss.subsurface((610, 736, 16, 16))
        self.axe = ss.subsurface((672, 721, 16, 16))
        self.shovel = ss.subsurface((672, 768, 16, 16))
