from data.animal import Animal
from data.leaves import Leaves
from lib.scene import Scene
from lib.tilemap import TileMap
import pygame

class Field(Scene):
    def __init__(self, core):
        self.core = core
        self.tilemap = TileMap(self.core, "data/scenes/field/field.json")
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
        if self.core.player.y >= self.core.screen.get_height():
            self.core.changeScene("home")
            self.core.scene.positionPlayer(True)

    def positionPlayer(self):
        self.core.player.y = self.core.screen.get_height() - 100

    def initClutter(self):
        self.clutterInit = True
