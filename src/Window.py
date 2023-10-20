import pygame
from Menu import Menu
from MainMenu import MainMenu

class Window:
    def __init__(self) -> None:
        pygame.init
        self.resolution = (1920, 1080)
        self.screen = pygame.display.set_mode(self.resolution, pygame.RESIZABLE) ##| pygame.FULLSCREEN)
        pygame.display.set_caption(" - PROJECT NSI TERMINALE - ", "")
        self.clock = pygame.time.Clock()

    def run(self):

        Running = True
        menu = MainMenu(self.resolution)

        while Running:
            self.clock.tick(60)
            self.afficherMenu(menu)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False

    def afficherMenu(self, menu:Menu):
        pass