import pygame
import time

class Button:
    def __init__(self, display, pos:tuple, width_height:tuple, col:tuple, col2:tuple, text:str, renvoi, underline = False) -> None:
        self.display = display
        font = pygame.font.SysFont("Arial", 30)
        font.set_underline(underline)
        self.pos = pos[0], pos[0] + width_height[0], pos[1], pos[1] + width_height[1]
        self.widht_height = width_height
        self.colours = col, col2
        self.text = font.render(text, True, (0,0,0)), pygame.font.Font.size(font, text)
        self.renvoi = renvoi
        self.underline = underline
        self.clicked = False

    def draw(self, clicked:bool):
        if not clicked:
            pygame.draw.rect(self.display, self.colours[1], pygame.Rect(self.pos[0], self.pos[2], self.widht_height[0], self.widht_height[1]),border_radius=12)
            pygame.draw.rect(self.display, self.colours[0], pygame.Rect(self.pos[0], self.pos[2] - 7, self.widht_height[0], self.widht_height[1]), border_radius=12)
            self.display.blit(self.text[0], (self.pos[0] + self.widht_height[0]/2 - self.text[1][0]/2, self.pos[2] + self.widht_height[1]/2 - self.text[1][1]/2 - 7))
        else:
            pygame.draw.rect(self.display, (0,0,0), pygame.Rect(self.pos[0], self.pos[2] - 7, self.widht_height[0], self.widht_height[1]))
            pygame.draw.rect(self.display, self.colours[0], pygame.Rect(self.pos[0], self.pos[2], self.widht_height[0], self.widht_height[1]), border_radius=12)
            self.display.blit(self.text[0], (self.pos[0] + self.widht_height[0]/2 - self.text[1][0]/2, self.pos[2] + self.widht_height[1]/2 - self.text[1][1]/2))

    def update(self, event):
        self.isClicked(event) 
        self.draw(self.clicked)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.clicked:
            self.clicked = False
            self.draw(self.clicked)
            if pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[0] < self.pos[1] and pygame.mouse.get_pos()[1] > self.pos[2]-7 and pygame.mouse.get_pos()[1] < self.pos[3]-7:
                time.sleep(0.1)
                return self.renvoi


    def isClicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                if pygame.mouse.get_pos()[0] > self.pos[0] and pygame.mouse.get_pos()[0] < self.pos[1] and pygame.mouse.get_pos()[1] > self.pos[2]-7 and pygame.mouse.get_pos()[1] < self.pos[3]-7:
                    self.clicked = True