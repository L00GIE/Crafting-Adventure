from lib.collider import Collider
import pygame

class Item:

    def __init__(self, core, tile, texture, type):
        self.core = core
        self.tile = tile
        self.texture = texture
        self.type = type
        self.w = 16
        self.h = 16
        self.x = self.tile.x + ((48 / 2) - (self.w / 2))
        self.y = self.tile.y + ((48 / 2) - (self.h / 2))
        self.starty = self.y
        self.collider = Collider(self, debug=False)
        self.goingup = True
        self.floatheight = 10

    def loop(self):
        self.float()
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        self.detectPickup()
        self.core.screen.blit(self.texture, (self.x, self.y))

    def float(self):
        if self.y > self.starty - self.floatheight and self.goingup:
            self.y -= 1
        elif self.y == self.starty - self.floatheight and self.goingup:
            self.goingup = False
        elif self.y < self.starty and not self.goingup:
            self.y += 1
        elif self.y == self.starty and not self.goingup:
            self.goingup = True

    def detectPickup(self):
        if self.core.player.collider.colliding(self):
            self.tile.item = None
            if self.type in self.core.player.inventory["items"]:
                self.core.player.inventory["items"][self.type] += 1
            else:
                self.core.player.inventory["items"][self.type] = 1
