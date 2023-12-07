from Menu import *
from Button import Button

class SceneMenu(Menu):
    
    def __init__(self, args) -> None:
        super().__init__(args)
        button_back = Button(self.display, (50, 50), (100, 70), (255, 255, 0), (255, 255, 255), '<==', 'back')
        button1 = Button(self.display, (200, 100), (200, 100), (255,255,0), (255,255,255), 'OK', 'OK')
        self.obj = [button_back, button1]

    
