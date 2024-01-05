import pygame
from data.player import Player
from data.scenes.test.test import test
from lib.cursor import Cursor

class Core:

    def __init__(self, screen):
        self.screen = screen
        self.cursor = None
        self.scene = None
        self.player = None
        self.initScenes()

    def loop(self, events):
        self.events = events

        if self.scene is None:
            self.scene = self.scenes[0]
        if self.player is None:
            self.player = Player(self)
            self.scene.add(self.player)

        self.scene.loop()
        if self.cursor is None:
            self.cursor = Cursor(self)
            self.scene.add(self.cursor)

    def initScenes(self):
        self.scenes = [
            test(self)
        ]
