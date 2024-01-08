import pygame
from data.item import Item
from data.plant import Plant
from lib.collider import Collider

class Tile:

    def __init__(self, core, pos, tileindex, rotation=0, barrier=None, trigger=False):
        self.core = core
        self.x = pos[0]
        self.y = pos[1]
        self.image = None
        self.tileindex = tileindex
        self.rotation = rotation * -1
        self.changeImage()
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        if barrier is None:
            self.barrier = self.checkBarrier()
        else:
            self.barrier = barrier
        self.trigger = trigger
        self.canplant = False
        self.candig = True
        self.plant = None
        self.item = None
        self.timer = 0
        self.collider = Collider(self, debug=False)

    def loop(self):
        self.timeDirt()
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        self.cursorInteract()
        self.playerInteract()
        self.core.screen.blit(self.image, (self.x, self.y))
        if self.plant is not None:
            self.plant.loop()
        if self.item is not None:
            self.item.loop()

    def timeDirt(self):
        if self.tileindex == 1 and self.plant is None and self.canplant: # if dirt but no plant start timer
            self.timer += 1
            if self.timer > 10000: # if timer reaches amount, turn back to grass
                self.tileindex = 0
                self.changeImage()
        else:
            self.timer = 0

    def cursorInteract(self):
        if self.core.cursor is None:
            return
        if self.core.cursor.collider.colliding(self): # cursor touching tile
            if self.tileindex == 0 and self.candig: # hovering over grass
                self.core.cursor.cursor = self.core.cursor.shovel
            elif self.tileindex == 3: # hovering over stump
                self.core.cursor.cursor = self.core.cursor.axe
            elif self.tileindex == 1 and self.canplant and self.plant is None: # hovering over empty, plantable dirt
                self.core.cursor.cursor = self.core.cursor.plant
            else:
                self.core.cursor.cursor = self.core.cursor.pointer
            
            for event in self.core.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0] and self.core.player.collider.colliding(self):
                        if self.tileindex == 0 and self.candig:
                            self.tileindex = 1 # if grass, make dirt
                            self.canplant = True
                        elif self.tileindex == 1 and self.canplant: # if dirt, add plant
                            self.addPlant()
                        elif self.tileindex == 3:
                            self.tileindex = 0 # if stump, make grass and drop wood
                            self.item = Item(self.core, self, self.core.texturemanager.wood, "wood")
                            self.barrier = False
                        self.changeImage()
                        self.barrier = self.checkBarrier()

    def playerInteract(self):
        if self.barrier:
            if self.core.player.collider.colliding(self):
                self.core.player.stop(self)

    def addPlant(self):
        if self.plant is None and self.core.player.inventory["seeds"][self.core.seedsUI.seedstring] > 0:
            plant = Plant(self.core, self, self.core.seedsUI.seedstring)
            self.core.player.inventory["seeds"][self.core.seedsUI.seedstring] -= 1
            self.plant = plant

    def changeImage(self):
        tiles = [
            self.core.texturemanager.grass,
            self.core.texturemanager.dirt,
            self.core.texturemanager.dirtedge,
            self.core.texturemanager.stump,
            self.core.texturemanager.fence,
            self.core.texturemanager.fenceend,
            self.core.texturemanager.fencecorner,
            self.core.texturemanager.fencecorneralt,
            self.core.texturemanager.forest,
            self.core.texturemanager.houseside,
            self.core.texturemanager.housesideend,
            self.core.texturemanager.woodfloor
        ]
        self.image = pygame.transform.rotate(tiles[self.tileindex], self.rotation)

    def checkBarrier(self):
        barriers = [3, 4, 5, 6, 7, 8]
        if self.tileindex in barriers:
            return True
        return False
        