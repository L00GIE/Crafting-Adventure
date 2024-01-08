import json, pygame
from lib.tile import Tile

class TileMap:

    def __init__(self, core, map):
        self.core = core
        self.map = map
        self.tiles = []
        self.processMap()

    def loop(self):
        for tile in self.tiles:
            tile.loop()

    def processMap(self):
        with open(self.map) as f:
            content = f.read()
        data = json.loads(content)
        tiledata = data["tiles"]
        rotationdata = data["rotations"]
        index = 0
        for y in range(16):
            for x in range(29):
                tile = Tile(self.core, (48 * x, 48 * y), tiledata[index], rotation=rotationdata[index])
                if tile.tileindex == 1:
                    tile.ispath = True
                self.tiles.append(tile)
                index += 1
