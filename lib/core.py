import pygame, pickle, os
from data.player import Player
from data.scenes.home.home import Home
from data.scenes.store.store import Store
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
        self.loaded = False
        self.initScenes()

    def loop(self, events):
        self.events = events

        if self.scene is None:
            self.scene = self.scenes["home"]
        if self.player is None:
            self.player = Player(self)
        if self.player not in self.scene.objects:
            self.scene.add(self.player)
        if self.seedsUI is None:
            self.seedsUI = SeedsUI(self)
        if self.seedsUI not in self.scene.objects:
            self.scene.add(self.seedsUI)
        if self.cursor is None:
            self.cursor = Cursor(self)
        if self.cursor not in self.scene.objects:
            self.scene.add(self.cursor)
        
        self.scene.loop()

        if os.path.exists("game.save") and not self.loaded:
            self.load()
            self.loaded = True

    def initScenes(self):
        self.scenes = {
            "home": Home(self),
            "town": Town(self),
            "store": Store(self)
        }

    def changeScene(self, scene):
        self.scene.remove(self.player)
        self.scene.remove(self.seedsUI)
        self.scene.remove(self.cursor)
        self.scene = self.scenes[scene]

    def save(self):
        savedata = {
            "inventory": self.player.inventory,
            "tiledata": {}
        }
        for scene in self.scenes:
            savedata["tiledata"][scene] = []
            if hasattr(self.scenes[scene], "tilemap"):
                if self.scenes[scene].tilemap is not None:
                    for tile in self.scenes[scene].tilemap.tiles:
                        savedata["tiledata"][scene].append(tile.tileindex)
        pickle.dump(savedata, open('game.save', 'wb'), protocol=pickle.HIGHEST_PROTOCOL)

    def load(self):
        savedata = pickle.load(open('game.save', 'rb'))
        self.player.inventory = savedata["inventory"]
        for scene in savedata["tiledata"]:
            index = 0
            for tileindex in savedata["tiledata"][scene]:
                if hasattr(self.scenes[scene], "tilemap"):
                    if self.scenes[scene].tilemap is not None:
                        tile = self.scenes[scene].tilemap.tiles[index]
                        tile.tileindex = tileindex
                        tile.barrier = tile.checkBarrier()
                        tile.changeImage()
                        index += 1
