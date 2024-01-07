from lib.collider import Collider
import pygame

class Plant:

    def __init__(self, core, tile, type):
        self.core = core
        self.tile = tile
        self.type = type
        self.w = 16
        self.h = 16
        self.x = self.tile.x + ((48 / 2) - (self.w / 2))
        self.y = self.tile.y + ((48 / 2) - (self.h / 2))
        self.starty = self.y
        self.stage = 1
        self.initSprite()
        self.collider = Collider(self, debug=False)
        self.timer = 0
        self.goingup = True
        self.floatheight = 10

    def loop(self):
        self.timer += 1
        if self.timer >= 1000:
            self.timer = 0
            if self.stage < 5:
                self.stage += 1
                self.initSprite()
        if self.stage >= 5:
            self.float()
            self.detectPickup()
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        self.core.screen.blit(self.sprite, (self.x, self.y))

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
            self.tile.plant = None
            self.core.player.inventory["crops"][self.type] += 1

    def initSprite(self):
        img = f"data/assets/Elements/Crops/{self.type}_0{self.stage}.png"
        self.sprite = pygame.image.load(img)
        self.sprite = pygame.transform.scale(self.sprite, (self.w, self.h))