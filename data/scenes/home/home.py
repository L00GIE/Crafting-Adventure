from data.animal import Animal
from data.leaves import Leaves
from lib.scene import Scene
from lib.tilemap import TileMap
import pygame

class Home(Scene):
    def __init__(self, core):
        self.core = core
        self.tilemap = TileMap(self.core, "data/scenes/home/home.json")
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
        if self.core.player.y < 1:
            self.core.player.y = 0
        if self.core.player.y >= self.core.screen.get_height() - self.core.player.h:
            self.core.player.y = self.core.screen.get_height() - self.core.player.h
        if self.core.player.x >= self.core.screen.get_width():
            self.core.changeScene("town")
            self.core.scene.positionPlayer()

    def positionPlayer(self):
        self.core.player.x = self.core.screen.get_width() - 100

    def initClutter(self):
        self.add(Animal(self.core, (1200, 700), "data/assets/Elements/Animals/spr_deco_cow_strip4.png"))
        self.add(Animal(self.core, (1100, 500), "data/assets/Elements/Animals/spr_deco_cow_strip4.png"))
        self.add(Animal(self.core, (200, 200), "data/assets/Elements/Animals/spr_deco_cow_strip4.png"))
        self.add(Animal(self.core, (300, 400), "data/assets/Elements/Animals/spr_deco_sheep_01_strip4.png"))
        self.add(Animal(self.core, (200, 300), "data/assets/Elements/Animals/spr_deco_cow_strip4.png"))
        self.add(Animal(self.core, (300, 300), "data/assets/Elements/Animals/spr_deco_sheep_01_strip4.png"))
        self.clutterInit = True
