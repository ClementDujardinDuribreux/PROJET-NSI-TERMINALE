from Menu import *
from Button import Button

class OptionMenu(Menu):

    def __init__(self, args: list) -> None:
        super().__init__(args)
        button_back = Button(self.display, (50, 50), (100, 70), (255, 255, 0), (255, 255, 255), '<==', 'back')
        self.obj = [button_back]