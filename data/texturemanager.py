import pygame

class TextureManager:
    
    def __init__(self):
        self.tileset = pygame.image.load("data/assets/Tileset/spr_tileset_sunnysideworld_16px.png")
        self.initTextures()

    def initTextures(self):
        self.grass = pygame.transform.scale(self.tileset.subsurface(32, 32, 32, 32), (48, 48)) # grass 0
        self.dirt = pygame.transform.scale(self.tileset.subsurface(320, 112, 32, 32), (48, 48)) # dirt 1
        self.dirtedge = pygame.transform.scale(self.tileset.subsurface(240, 32, 16, 16), (48, 48)) # dirt edge 2
        self.stump = pygame.transform.scale(self.tileset.subsurface(512, 80, 16, 16), (48, 48)) # stump 3
        self.fence = pygame.transform.scale(self.tileset.subsurface(623, 32, 16, 16), (48, 48)) # fence 4
        self.fenceend = pygame.transform.scale(self.tileset.subsurface(607, 32, 16, 16), (48, 48)) # fence end 5
        self.fencecorner = pygame.transform.scale(self.tileset.subsurface(608, 16, 16, 16), (48, 48)) # fence corner 6
        self.fencecorneralt = pygame.transform.scale(self.tileset.subsurface(656, 16, 16, 16), (48, 48)) # fence corner alt 7
        self.forest = pygame.transform.scale(self.tileset.subsurface(816, 16, 32, 32), (48, 48)) # forest 8
        self.houseside = pygame.transform.scale(self.tileset.subsurface(304, 320, 16, 16), (48, 48)) # green house side 9
        self.housesideend = pygame.transform.scale(self.tileset.subsurface(304, 336, 16, 16), (48, 48)) # green house side end 10
        self.woodfloor = pygame.transform.scale(self.tileset.subsurface(160, 160, 16, 16), (48, 48)) # wooden floor 11
        self.green_building = pygame.transform.scale_by(self.tileset.subsurface(520, 290, 32, 64), 3)