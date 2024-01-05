import pygame
from lib.collider import Collider

class Building:

    def __init__(self, core, img, scene, pos):
        self.core = core
        self.x = pos[0]
        self.y = pos[1]
        self.image = img
        self.scene = scene
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.collider = Collider(self)

    def loop(self):
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        self.checkCollision()
        self.core.screen.blit(self.image, (self.x, self.y))

    def checkCollision(self):
        if self.core.player is None:
            return
        if self.core.player.collider.colliding(self):
            self.core.changeScene(self.scene)