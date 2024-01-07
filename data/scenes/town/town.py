from data.building import Building
from data.leaves import Leaves
from lib.scene import Scene
import pygame

from lib.tilemap import TileMap

class Town(Scene):

    def __init__(self, core):
        self.core = core
        self.tilemap = TileMap(self.core, "data/scenes/town/town.json")
        for tile in self.tilemap.tiles:
            tile.candig = False
        self.clutterInit = False
        self.leaves = None
        super().__init__()

    def loop(self):
        self.core.screen.fill([99, 199, 77])
        if self.tilemap not in self.objects:
            self.add(self.tilemap, behindplayer=True)
        if self.leaves is None:
            self.leaves = Leaves(self.core)
            self.add(self.leaves)
        if not self.clutterInit:
            self.initClutter()
        self.checkpos()
        super().loop()

    def checkpos(self):
        if self.core.player.x <= 0:
            self.core.changeScene("home")
            self.core.scene.positionPlayer()

    def positionPlayer(self, shop=False):
        if shop:
            self.core.player.x = 600
            self.core.player.y = 200
        else:
            self.core.player.x = 100

    def initClutter(self):
        self.add(Building(self.core, self.core.texturemanager.green_building, "store", (600, 0)))
        self.clutterInit = True
