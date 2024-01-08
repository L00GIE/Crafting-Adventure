import pygame

class SeedsUI:
    def __init__(self, core):
        self.core = core
        self.x = 0
        self.y = 0
        self.sprite = pygame.transform.scale(pygame.image.load("data/assets/UI/seed-bag.png"), (200, 200))
        self.w = self.sprite.get_width()
        self.h = self.sprite.get_height()
        self.selected = 0
        self.seedsprite = None
        self.seedtext = None
        self.seedstring = None
        self.font = pygame.font.SysFont("Helvetica", 16)

    def loop(self):
        for event in self.core.events:
            if event.type == pygame.MOUSEWHEEL:
                self.selected += event.y
                self.changeseed()
        self.core.screen.blit(self.sprite, (0, 0))
        self.showseed()

    def showseed(self):
        if self.seedsprite is None:
            self.changeseed()
        self.core.screen.blit(self.seedsprite, ((self.x + ((self.w / 2) - (self.seedsprite.get_width() / 2))), self.y + 50))
        self.core.screen.blit(self.seedtext, ((self.x + ((self.w / 2) - (self.seedtext.get_width() / 2))), self.y + 125))
        counttext = self.font.render(f"x{self.core.player.inventory['seeds'][self.seedstring]}", True, [0, 0, 0])
        self.core.screen.blit(counttext, ((self.x + ((self.w / 2) - (counttext.get_width() / 2))), self.y + 145))
            
    def changeseed(self):
        seeds = [
            "beetroot",
            "cabbage",
            "carrot",
            "cauliflower",
            "kale",
            "parsnip",
            "potato",
            "pumpkin",
            "radish",
            "sunflower",
            "wheat"
        ]
        if self.selected < 0:
            self.selected = len(seeds) - 1
        if self.selected >= len(seeds):
            self.selected = 0
        self.seedsprite = pygame.transform.scale(pygame.image.load(f"data/assets/Elements/Crops/{seeds[self.selected]}_00.png"), (48, 48))
        self.seedtext = self.font.render(seeds[self.selected].capitalize(), True, [0, 0, 0])
        self.seedstring = seeds[self.selected]
