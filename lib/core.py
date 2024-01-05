import pygame
from data.player import Player
from data.scenes.test.test import test
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
            self.scene = self.scenes[0]
        if self.player is None:
            self.player = Player(self)
        if self.player not in self.scene.objects:
            self.scene.add(self.player)
        if self.seedsUI is None:
            self.seedsUI = SeedsUI(self)
        if self.seedsUI not in self.scene.objects:
            self.scene.add(self.seedsUI)

        self.scene.loop()
        if self.cursor is None:
            self.cursor = Cursor(self)
            self.scene.add(self.cursor)

    def initScenes(self):
        self.scenes = [
            test(self)
        ]
