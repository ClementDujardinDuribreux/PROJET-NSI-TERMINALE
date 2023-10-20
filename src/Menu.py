from Button import Button

class Menu:
    def __init__(self, resolution:tuple) -> None:
        self.res = resolution
        self.listeButton = []

    def afficher(self):
        pass
    
    def CreateButton(self, pos_x:int, pos_y:int, longueur:int, largeur:int, col:int, txt:str, renvoi:object):
        button = Button(pos_x, pos_y, longueur, largeur, col, txt, renvoi)
        self.listeButton.append(button)
        return None