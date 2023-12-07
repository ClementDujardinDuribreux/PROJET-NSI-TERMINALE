from Menu import *
from SceneMenu import SceneMenu
from OptionMenu import OptionMenu
from Button import Button

class MainMenu(Menu):

    def __init__(self, args) -> None:
        super().__init__(args)
        button_play = Button(self.display, (RES[0]*0.2, RES[1]*0.15), (RES[0]*0.6, RES[1]*0.15), (255,255,0), (255,255,255), 'JOUER', SceneMenu(args))
        button_option = Button(self.display, (RES[0]*0.2, RES[1]*0.40), (RES[0]*0.6, RES[1]*0.15), (255,255,0), (255,255,255), 'OPTIONS', OptionMenu(args))
        button_quit = Button(self.display, (RES[0]*0.2, RES[1]*0.65), (RES[0]*0.6, RES[1]*0.15), (255,255,0), (255,255,255), 'QUITTER', 'quit')

        self.obj = [button_play, button_option, button_quit]
