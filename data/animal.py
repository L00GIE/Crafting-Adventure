import pygame, random
from lib.animation import Animation
from lib.collider import Collider

class Animal:

    def __init__(self, core, pos, spritesheet):
        self.core = core
        self.x = pos[0]
        self.y = pos[1]
        self.w = 64
        self.h = 64
        self.speed = 10
        self.collider = Collider(self, debug=False)
        self.spritesheet = spritesheet
        self.initSprites()
        self.currentAnim = self.anim

    def loop(self):
        self.wanderAimlessly()
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        if self.core.player.collider.colliding(self):
            self.core.player.stop(self)
        self.currentAnim.play()

    def stop(self, tile):
        if self.collider.rect.right >= tile.collider.rect.left and \
            self.collider.rect.left < tile.collider.rect.left:
            self.x -= self.speed
        elif self.collider.rect.left <= tile.collider.rect.right and \
            self.collider.rect.right > tile.collider.rect.right:
            self.x += self.speed
        if self.collider.rect.bottom >= tile.collider.rect.top and \
            self.collider.rect.top < tile.collider.rect.top:
            self.y -= self.speed
        elif self.collider.rect.top <= tile.collider.rect.bottom and \
            self.collider.rect.bottom > tile.collider.rect.bottom:
            self.y += self.speed

    def wanderAimlessly(self):
        self.stayInScene()
        if random.randint(1, 100) == 1:
            direction = random.randint(0, 3)
            if direction == 0:
                self.x += self.speed
                self.currentAnim = self.animFlipped
            elif direction == 1:
                self.x -= self.speed
                self.currentAnim = self.anim
            elif direction == 2:
                self.y -= self.speed
                self.currentAnim = self.anim
            elif direction == 3:
                self.y -= self.speed
                self.currentAnim = self.animFlipped
        if self.core.scene == self.core.scenes["home"]:
            for tile in self.core.scene.tilemap.tiles:
                if self.collider.colliding(tile) and tile.barrier:
                    self.stop(tile)

    def stayInScene(self):
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0
        if self.x > self.core.screen.get_width() - self.w:
            self.x = self.core.screen.get_width() - self.w
        if self.y > self.core.screen.get_height() - self.h:
            self.y = self.core.screen.get_height() - self.h

    def initSprites(self):
        strip = pygame.image.load(self.spritesheet)
        sprites = []
        for x in range(4):
            sprites.append(strip.subsurface((32 * x, 0, 32, 32)))
        self.anim = Animation(self.core, sprites, self, delay=10)
        self.animFlipped = Animation(self.core, sprites, self, delay=10, flipx=True)