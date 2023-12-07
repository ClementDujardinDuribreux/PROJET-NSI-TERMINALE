import pygame
from OPTIONS import*

class Menu:

    def __init__(self, args:list) -> None:
        self.display = args[0]
        self.obj = []

    def update(self, event):
        retour = []
        for item in self.obj:
            retour.append(item.update(event))
        pygame.display.flip()
        return retour

    def get_escape(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return True
        return False