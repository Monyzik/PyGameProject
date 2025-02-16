import pygame


class Score(object):
    def __init__(self):
        self.black: pygame.Color = pygame.Color(0, 0, 0)
        self.count = 0
        self.font = pygame.font.SysFont(None, 45)
        self.text = self.font.render("Score : " + str(self.count), 1, self.black)

    def show_score(self, screen):
        screen.blit(self.text, (20, 75))

    def score_up(self):
        self.count += 10
        self.text = self.font.render("Score : " + str(self.count), 1, self.black)
