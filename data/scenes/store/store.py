from data.animal import Animal
from lib.scene import Scene
from lib.tilemap import TileMap
import pygame

class Store(Scene):
    def __init__(self, core):
        self.core = core
        self.tilemap = TileMap(self.core, "data/scenes/store/store.json")
        self.clutterInit = False
        super().__init__()

    def loop(self):
        self.core.screen.fill([99, 199, 77])
        if self.tilemap not in self.objects:
            self.add(self.tilemap, behindplayer=True)
        if not self.clutterInit:
            self.initClutter()
        self.checkpos()
        super().loop()

    def checkpos(self):
        if self.core.player.y >= self.core.screen.get_height():
            self.core.changeScene("town")
            self.core.scene.positionPlayer(shop=True)

    def positionPlayer(self):
        self.core.player.x = (self.core.screen.get_width() / 2) - (self.core.player.w / 2)
        self.core.player.y = self.core.screen.get_height() - 100

    def initClutter(self):
        self.clutterInit = True
