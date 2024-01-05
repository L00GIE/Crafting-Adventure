from data.animal import Animal
from lib.scene import Scene
from lib.tilemap import TileMap
import pygame

class Home(Scene):
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
        if self.core.player.x >= self.core.screen.get_width():
            self.core.changeScene("town")

    def positionPlayer(self):
        self.core.player.x = self.core.screen.get_width() - 100

    def initTilemap(self):
        self.tilemap = TileMap(self.core, "data/scenes/home/home.json")
        self.add(self.tilemap, behindplayer=True)

    def initClutter(self):
        self.add(Animal(self.core, (1200, 700), "data/assets/Elements/Animals/spr_deco_cow_strip4.png"))
        self.add(Animal(self.core, (1100, 500), "data/assets/Elements/Animals/spr_deco_cow_strip4.png"))
        self.add(Animal(self.core, (200, 200), "data/assets/Elements/Animals/spr_deco_cow_strip4.png"))
        self.add(Animal(self.core, (300, 400), "data/assets/Elements/Animals/spr_deco_cow_strip4.png"))
        self.clutterInit = True
