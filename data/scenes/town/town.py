from lib.scene import Scene
import pygame

from lib.tilemap import TileMap

class Town(Scene):

    def __init__(self, core):
        self.core = core
        self.tilemap = None
        self.clutterInit = False
        super().__init__()

    def loop(self):
        self.core.screen.fill([99, 199, 77])
        if self.tilemap is None:
            self.initTilemap()
        if not self.clutterInit:
            self.initClutter()
        self.checkpos()
        super().loop()

    def checkpos(self):
        if self.core.player.x <= 0:
            self.core.changeScene("home")

    def positionPlayer(self):
        self.core.player.x = 100

    def initTilemap(self):
        self.tilemap = TileMap(self.core, "data/scenes/town/town.json")
        self.add(self.tilemap, behindplayer=True)

    def initClutter(self):
        self.clutterInit = True
