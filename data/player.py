import pygame
from data.inventoryui import InventoryUI
from lib.animation import Animation
from lib.collider import Collider

class Player:

    def __init__(self, core):
        self.core = core
        self.x = 600
        self.y = 400
        self.w = 64
        self.h = 64
        self.speed = 3
        self.minspeed = 3
        self.maxspeed = 5
        self.running = False
        self.collider = Collider(self, debug=False)
        self.initSprites()
        self.initInventory()

    def loop(self):
        self.idle()
        self.checkMoving()
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        self.currentanim.play()
        self.currenthairanim.play()

    def checkMoving(self):
        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        if mods & pygame.KMOD_LSHIFT:
            self.running = True
            self.speed = self.maxspeed
        else:
            self.running = False
            self.speed = self.minspeed
        if keys[pygame.K_w]:
            self.move("y", self.speed * -1)
        if keys[pygame.K_s]:
            self.move("y", self.speed)
        if keys[pygame.K_a]:
            self.move("x", self.speed * -1)
        if keys[pygame.K_d]:
            self.move("x", self.speed)

    def move(self, axis, delta):
        if axis == "y":
            self.y += delta
        elif axis == "x":
            self.x += delta
        if delta < 0:
            self.walk(True)
        else:
            self.walk()

    def idle(self):
        self.currentanim = self.idleAnim
        self.currenthairanim = self.idleHairAnim

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

    def walk(self, left=False):
        if left:
            if self.running:
                self.currentanim = self.runLeftAnim
                self.currenthairanim = self.runLeftHairAnim
                return
            self.currentanim = self.walkLeftAnim
            self.currenthairanim = self.walkLeftHairAnim
        else:
            if self.running:
                self.currentanim = self.runRightAnim
                self.currenthairanim = self.runRightHairAnim
                return
            self.currentanim = self.walkRightAnim
            self.currenthairanim = self.walkRightHairAnim

    def initInventory(self):
        self.inventory = {
            "seeds": {
                "beetroot": 20,
                "cabbage": 20,
                "carrot": 20,
                "cauliflower": 20,
                "kale": 20,
                "parsnip": 20,
                "potato": 20,
                "pumpkin": 20,
                "radish": 20,
                "sunflower": 20,
                "wheat": 20
            },
            "crops": {
                "beetroot": 0,
                "cabbage": 0,
                "carrot": 0,
                "cauliflower": 0,
                "kale": 0,
                "parsnip": 0,
                "potato": 0,
                "pumpkin": 0,
                "radish": 0,
                "sunflower": 0,
                "wheat": 0
            },
            "items": {
                "wood": 10,
                "milk": 5
            },
            "money": 60.00
        }

    def initSprites(self):
        idlestrip = pygame.image.load("data/assets/Characters/Human/IDLE/base_idle_strip9.png")
        idlehairstrip = pygame.image.load("data/assets/Characters/Human/IDLE/bowlhair_idle_strip9.png")
        walkstrip = pygame.image.load("data/assets/Characters/Human/WALKING/base_walk_strip8.png")
        walkhairstrip = pygame.image.load("data/assets/Characters/Human/WALKING/bowlhair_walk_strip8.png")
        runstrip = pygame.image.load("data/assets/Characters/Human/RUN/base_run_strip8.png")
        runhairstrip = pygame.image.load("data/assets/Characters/Human/RUN/bowlhair_run_strip8.png")
        xcoords = [39, 135, 231, 327, 423, 519, 615, 711, 807]
        animdelay = 5
        sprites = []
        for x in xcoords:
            sprites.append(idlestrip.subsurface(x, 19, 20, 25))
        self.idleAnim = Animation(self.core, sprites, self, delay=animdelay)
        sprites = []
        for x in xcoords:
            sprites.append(idlehairstrip.subsurface(x, 19, 20, 25))
        self.idleHairAnim = Animation(self.core, sprites, self, delay=animdelay)
        sprites = []
        for x in range(7):
            sprites.append(walkstrip.subsurface(xcoords[x], 19, 20, 25))
        self.walkLeftAnim = Animation(self.core, sprites, self, delay=animdelay, flipx=True)
        self.walkRightAnim = Animation(self.core, sprites, self, delay=animdelay)
        sprites = []
        for x in range(7):
            sprites.append(walkhairstrip.subsurface(xcoords[x], 19, 20, 25))
        self.walkLeftHairAnim = Animation(self.core, sprites, self, delay=animdelay, flipx=True)
        self.walkRightHairAnim = Animation(self.core, sprites, self, delay=animdelay)
        sprites = []
        for x in range(7):
            sprites.append(runstrip.subsurface(xcoords[x], 19, 20, 25))
        self.runLeftAnim = Animation(self.core, sprites, self, delay=animdelay, flipx=True)
        self.runRightAnim = Animation(self.core, sprites, self, delay=animdelay)
        sprites = []
        for x in range(7):
            sprites.append(runhairstrip.subsurface(xcoords[x], 19, 20, 25))
        self.runLeftHairAnim = Animation(self.core, sprites, self, delay=animdelay, flipx=True)
        self.runRightHairAnim = Animation(self.core, sprites, self, delay=animdelay)
