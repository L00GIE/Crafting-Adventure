import pygame

class Collider:

    def __init__(self, parent, debug=False):
        self.x, self.y, self.w, self.h = parent.x, parent.y, parent.w, parent.h
        self.parent = parent
        self.rect = pygame.Rect((self.x, self.y, self.w, self.h))
        self.debug = debug

    def updaterect(self, x, y, w, h):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.w = self.w
        self.rect.h = self.h
        if self.debug:
            colliderrect = pygame.Rect(self.x - 2, self.y - 2, self.w + 4, self.h + 4)
            pygame.draw.rect(self.parent.core.screen, [255, 0, 0], colliderrect, width=2) # draw red rectangle around collider

    def colliding(self, obj):
        if hasattr(obj, "collider"):
            if self.rect.colliderect(obj.collider.rect):
                return True
        return False
