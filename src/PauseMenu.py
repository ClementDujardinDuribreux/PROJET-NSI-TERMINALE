import pygame
from OPTIONS import *
from Menu import Menu
from SceneMenu import SceneMenu
from MainMenu import MainMenu
from Button import Button

class PauseMenu(Menu):

    def __init__(self, args: list) -> None:
        super().__init__(args)
        button_play = Button(self.display, (RES[0]*0.2, RES[1]*0.15), (RES[0]*0.6, RES[1]*0.15), (255,255,0), (255,255,255), 'REPRENDRE', 'back')
        button_restart = Button(self.display, (RES[0]*0.2, RES[1]*0.40), (RES[0]*0.6, RES[1]*0.15), (255,255,0), (255,255,255), 'RELANCER', SceneMenu(args))
        button_quit = Button(self.display, (RES[0]*0.2, RES[1]*0.65), (RES[0]*0.6, RES[1]*0.15), (255,255,0), (255,255,255), 'MENU PRINCIPAL', 'back_to_MainMenu')

        self.obj = [button_play, button_restart, button_quit]

    def draw(self):
        pygame.draw.rect(self.display, (0,0,0,0), pygame.Rect(0, 0, RES[0], RES[1]))