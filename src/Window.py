import pygame
from Sql import Sql
from Menu import Menu
from MainMenu import MainMenu
from ConnectionMenu import ConnectionMenu

class Window:
    def __init__(self, resolution:tuple) -> None:
        pygame.init()
        self.resolution = resolution
        self.screen = pygame.display.set_mode(self.resolution, pygame.RESIZABLE) ##| pygame.FULLSCREEN)
        pygame.display.set_caption(" - PROJECT NSI TERMINALE - ", "")
        self.clock = pygame.time.Clock()

    def run(self):

        Running = True
        menu = ConnectionMenu(self.resolution)
        sql = Sql()

        while Running:
            self.clock.tick(60)
            self.afficherMenu(menu)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Running = False

    def afficherMenu(self, menu:Menu):
        pass