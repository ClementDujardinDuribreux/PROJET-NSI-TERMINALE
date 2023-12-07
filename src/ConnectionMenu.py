import pygame
from Menu import Menu

class ConnectionMenu(Menu):
    def __init__(self, screen, resolution: tuple) -> None:
        Menu.__init__(self, screen, resolution)

        
    def demande(self, event):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True