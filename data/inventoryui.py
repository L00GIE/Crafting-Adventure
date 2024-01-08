import pygame

class InventoryUI:

    def __init__(self, core):
        self.core = core
        self.showing = False
        self.bg = pygame.image.load("data/assets/UI/tablet.png")
        self.moneybg = pygame.transform.scale_by(pygame.image.load("data/assets/UI/tablet2.png"), 0.5)
        self.font = pygame.font.SysFont("Helvetica", 16)
        self.x = self.core.screen.get_width() - self.bg.get_width()
        self.y = 0

    def loop(self):
        for event in self.core.events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_e:
                    self.openInventory()
        if self.showing:
            self.core.scene.paused = True
            self.core.cursor.cursor = self.core.cursor.pointer
            self.showInventory()
            self.showMoney()
        else:
            self.core.scene.paused = False

    def showInventory(self):
        self.core.screen.blit(self.bg, (self.x, self.y))
        seedtitle = pygame.transform.scale_by(self.font.render("Seeds", True, [0, 0, 0]), 1.5)
        self.core.screen.blit(seedtitle, (self.x + 200, self.y + 75))
        index = 0
        for seedtype in self.core.player.inventory["seeds"]:
            img = pygame.transform.scale(pygame.image.load(f"data/assets/Elements/Crops/{seedtype}_00.png"), (32, 32))
            title = self.font.render(f"{seedtype.capitalize()} x{self.core.player.inventory['seeds'][seedtype]}", True, [0, 0, 0])
            self.core.screen.blit(img, (self.x + 200, ((img.get_height() + 20) * index) + 120))
            self.core.screen.blit(title, (self.x + 210 + img.get_width(), ((img.get_height() + 20) * index) + 120))
            index += 1
        croptitle = pygame.transform.scale_by(self.font.render("Crops", True, [0, 0, 0]), 1.5)
        self.core.screen.blit(croptitle, (self.x + 400, self.y + 75))
        index = 0
        for croptype in self.core.player.inventory["crops"]:
            img = pygame.transform.scale(pygame.image.load(f"data/assets/Elements/Crops/{croptype}_05.png"), (32, 32))
            title = self.font.render(f"{croptype.capitalize()} x{self.core.player.inventory['crops'][croptype]}", True, [0, 0, 0])
            self.core.screen.blit(img, (self.x + 400, ((img.get_height() + 20) * index) + 120))
            self.core.screen.blit(title, (self.x + 410 + img.get_width(), ((img.get_height() + 20) * index) + 120))
            index += 1
        itemstitle = pygame.transform.scale_by(self.font.render("Items", True, [0, 0, 0]), 1.5)
        self.core.screen.blit(itemstitle, (self.x + 600, self.y + 75))
        index = 0
        for item in self.core.player.inventory["items"]:
            img = pygame.transform.scale(pygame.image.load(f"data/assets/Elements/Crops/{item}.png"), (32, 32))
            title = self.font.render(f"{item.capitalize()} x{self.core.player.inventory['items'][item]}", True, [0, 0, 0])
            self.core.screen.blit(img, (self.x + 600, ((img.get_height() + 20) * index) + 120))
            self.core.screen.blit(title, (self.x + 610 + img.get_width(), ((img.get_height() + 20) * index) + 120))
            index += 1

    def showMoney(self):
        self.core.screen.blit(self.moneybg, (10, self.core.screen.get_height() - self.moneybg.get_height()))
        img = pygame.transform.scale(pygame.image.load(f"data/assets/UI/money.png"), (32, 32))
        title = self.font.render(f"{round(self.core.player.inventory['money'], 2)}", True, [0, 0, 0])
        self.core.screen.blit(img, (100, self.core.screen.get_height() - ((self.moneybg.get_height() / 2) + (img.get_height() / 2))))
        self.core.screen.blit(title, (150, self.core.screen.get_height() - ((self.moneybg.get_height() / 2) + (title.get_height() / 2))))
        
    def openInventory(self):
        if self.showing:
            self.hide()
        else:
            self.show()

    def show(self):
        self.showing = True
        self.core.paused = True

    def hide(self):
        self.showing = False
        self.core.paused = False