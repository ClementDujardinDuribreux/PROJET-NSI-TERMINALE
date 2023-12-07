class Input:
    def __init__(self, screen, pos_x:int, pos_y:int, longueur:int, largeur:int) -> None:
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.longueur = longueur
        self.largeur = largeur

    def draw(self):
        pass

    def retour(self, event):
        pass