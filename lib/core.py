import pygame
from data.player import Player
from data.scenes.home.home import Home
from data.scenes.town.town import Town
from data.seedsui import SeedsUI
from data.texturemanager import TextureManager
from lib.cursor import Cursor

class Core:

    def __init__(self, screen):
        self.screen = screen
        self.cursor = None
        self.scene = None
        self.player = None
        self.seedsUI = None
        self.texturemanager = TextureManager()
        self.initScenes()

    def loop(self, events):
        self.events = events

        if self.scene is None:
            self.scene = self.scenes["home"]
        if self.player is None:
            self.player = Player(self)
        if self.player not in self.scene.objects:
            self.scene.add(self.player)
            self.scene.positionPlayer()
        if self.seedsUI is None:
            self.seedsUI = SeedsUI(self)
        if self.seedsUI not in self.scene.objects:
            self.scene.add(self.seedsUI)
        if self.cursor is None:
            self.cursor = Cursor(self)
        if self.cursor not in self.scene.objects:
            self.scene.add(self.cursor)

        self.scene.loop()

    def initScenes(self):
        self.scenes = {
            "home": Home(self),
            "town": Town(self)
        }

    def changeScene(self, scene):
        self.scene.remove(self.player)
        self.scene.remove(self.seedsUI)
        self.scene.remove(self.cursor)
        self.scene = self.scenes[scene]
