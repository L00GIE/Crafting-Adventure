import pygame

class Animation:

    def __init__(self, core, sprites, parent, delay=3, flipx=False):
        self.core = core
        self.sprites = sprites
        self.parent = parent
        self.flipx = flipx
        self.currentframe = 0
        self.delay = delay
        self.delaycount = 0
        self.ended = False

    def play(self):
        self.ended = False
        img = self.sprites[self.currentframe]
        if self.flipx:
            img = pygame.transform.flip(self.sprites[self.currentframe], True, False)
        img = pygame.transform.scale(img, (self.parent.w, self.parent.h))
        self.core.screen.blit(img, (self.parent.x, self.parent.y))
        if self.delaycount >= self.delay:
            self.delaycount = 0
            self.currentframe += 1
            if self.currentframe >= len(self.sprites):
                self.currentframe = 0
                self.ended = True
        self.delaycount += 1
        