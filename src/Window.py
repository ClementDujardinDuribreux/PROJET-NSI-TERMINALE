import pygame
import pyautogui
from OPTIONS import *
from MainMenu import MainMenu
from SceneMenu import SceneMenu
from PauseMenu import PauseMenu
from Button import Button
from Pile import Pile

class Window:
    def __init__(self) -> None:
        pygame.init()
        if FULLSCREEN:
            self.display = pygame.display.set_mode(RES, pygame.RESIZABLE | pygame.FULLSCREEN)
        else : self.display = pygame.display.set_mode(RES, pygame.RESIZABLE)
        pygame.display.set_caption(" - PROJECT NSI TERMINALE - ", "")
        self.clock = pygame.time.Clock()
        self.display_options = [self.display]
        self.scene = MainMenu(self.display_options)
        self.pile_pre_scene = Pile()
        self.draw_pause_scene = False
        self.pause_scene = PauseMenu(self.display_options)

    def run(self):

        Running = True
        while Running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.update(event)
                if type(self.scene) is type(SceneMenu(['','',''])) or type(self.scene) is type(self.pause_scene):
                    if self.scene.get_escape(event):
                        if not self.draw_pause_scene:
                            self.draw_pause_scene = True
                            self.change_scene_if('pause')
                        else:
                            self.draw_pause_scene = False
                            self.change_scene_if('back')
                else:
                    if self.scene.get_escape(event):
                        Running = False
                
                
                if event.type == pygame.QUIT:
                        Running = False      
            pygame.display.flip()
        pygame.quit()

    def update(self, event):
        return_item_scene = self.scene.update(event)
        for return_item in return_item_scene:
            self.change_scene_if(return_item)
        
    def change_scene_if(self, return_item):
        dico = {'quit': 0, 'back': 1, 'pause':2, 'back_to_MainMenu':3}
        if return_item in dico.keys():
            if dico[return_item] == 0:
                pygame.quit()
            if dico[return_item] == 1:
                self.update_scene()
                self.scene = self.pile_pre_scene.depiler()
                self.draw_pause_scene = False
            if dico[return_item] == 2:
                self.pile_pre_scene.empiler(self.scene)
                self.scene = self.pause_scene
                self.scene.draw()
            if dico[return_item] == 3:
                self.scene = MainMenu(self.display_options)
                self.pile_pre_scene = Pile()
                self.draw_pause_scene = False
                self.update_scene()
        elif return_item is not None:
            self.update_scene()
            if self.scene is not self.pause_scene:
                self.pile_pre_scene.empiler(self.scene)
            self.scene = return_item
            pre_scene = self.pile_pre_scene.depiler()
            if type(self.scene) != type(pre_scene):
                self.pile_pre_scene.empiler(pre_scene)
            self.draw_pause_scene = False

    def update_scene(self):
        self.display.fill((0,0,0))
        pygame.display.update()
        pyautogui.moveTo(pyautogui.position()[0] + 1)
