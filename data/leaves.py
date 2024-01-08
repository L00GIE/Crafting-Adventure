import pygame, random

class Leaves:

    def __init__(self, core):
        self.core = core
        self.leaf = pygame.image.load("data/assets/Elements/Other/leaf.png")
        self.leaves = []

    def loop(self):
        for leaf in self.leaves:
            leaf.loop()
            if leaf.y >= self.core.screen.get_height():
                self.leaves.remove(leaf)
        if len(self.leaves) < 20 and random.randint(1, 40) == 1:
            randx = random.randint(0, self.core.screen.get_width())
            self.leaves.append(Leaf(self.core, self.leaf, (randx, 0)))


class Leaf:

    def __init__(self, core, img, pos):
        self.core = core
        self.img = img
        self.x = pos[0]
        self.startx = self.x
        self.y = pos[1]
        self.speed = 1
        self.goingleft = False

    def loop(self):
        self.y += self.speed
        if self.goingleft:
            self.x -= self.speed
            if self.x <= self.startx - 50:
                self.goingleft = False
        else:
            self.x += self.speed
            if self.x >= self.startx + 50:
                self.goingleft = True
        if self.y < self.core.screen.get_height():
            self.core.screen.blit(self.img, (self.x, self.y))
