from Menu import Menu

class SkinMenu(Menu):
    def __init__(self, screen, resolution: tuple) -> None:
        Menu.__init__(self, screen, resolution)