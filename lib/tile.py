import pygame
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
        self.plant = None
        self.collider = Collider(self, debug=False)

    def loop(self):
        self.collider.updaterect(self.x, self.y, self.w, self.h)
        self.cursorInteract()
        self.playerInteract()
        self.core.screen.blit(self.image, (self.x, self.y))
        if self.plant is not None:
            self.plant.loop()

    def cursorInteract(self):
        if self.core.cursor is None:
            return
        if self.core.cursor.collider.colliding(self):
            if self.tileindex == 0: # hovering over grass
                self.core.cursor.cursor = self.core.cursor.shovel
            elif self.tileindex == 3: # hovering over stump
                self.core.cursor.cursor = self.core.cursor.axe
            else:
                self.core.cursor.cursor = self.core.cursor.pointer
            self.highlight()
            
            for event in self.core.events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        if self.tileindex == 0:
                            self.tileindex = 1 # if grass, make dirt
                            self.canplant = True
                        elif self.tileindex == 1 and self.canplant: # if dirt, add plant
                            self.addPlant()
                        elif self.tileindex == 3:
                            self.tileindex = 0 # if stump, make grass
                        self.changeImage()
                        self.barrier = self.checkBarrier()

    def playerInteract(self):
        if self.barrier:
            if self.core.player.collider.colliding(self):
                self.core.player.stop(self)

    def highlight(self):
        highlightrect = pygame.Rect(self.x - 2, self.y - 2, self.w + 4, self.h + 4)
        pygame.draw.rect(self.core.screen, [0, 0, 0], highlightrect, 2)

    def addPlant(self):
        if self.plant is None:
            plant = Plant(self.core, self, "beetroot")
            self.plant = plant

    def changeImage(self):
        ss = pygame.image.load("data/assets/Tileset/spr_tileset_sunnysideworld_16px.png")
        tiles = [
            pygame.transform.scale(ss.subsurface(32, 32, 32, 32), (48, 48)), # grass 0
            pygame.transform.scale(ss.subsurface(320, 112, 32, 32), (48, 48)), # dirt 1
            pygame.transform.scale(ss.subsurface(240, 32, 16, 16), (48, 48)), # dirt edge 2
            pygame.transform.scale(ss.subsurface(512, 80, 16, 16), (48, 48)), # stump 3
            pygame.transform.scale(ss.subsurface(623, 32, 16, 16), (48, 48)), # fence 4
            pygame.transform.scale(ss.subsurface(607, 32, 16, 16), (48, 48)), # fence end 5
            pygame.transform.scale(ss.subsurface(608, 16, 16, 16), (48, 48)), # fence corner 6
            pygame.transform.scale(ss.subsurface(656, 16, 16, 16), (48, 48)), # fence corner alt 7
            pygame.transform.scale(ss.subsurface(816, 16, 32, 32), (48, 48)), # forest 8
        ]
        self.image = pygame.transform.rotate(tiles[self.tileindex], self.rotation)

    def checkBarrier(self):
        barriers = [3, 4, 5, 6, 7, 8]
        if self.tileindex in barriers:
            return True
        return False
        