import pygame as pg

class UIWindow:
    def __init__(self):
        pass

    @staticmethod
    def render():
        pg.init()
        pg.display.set_caption('Game of Life')
        pg.font.init()
        font = pg.font.SysFont('Times New Roman', 40)
        extract_text = font.render('Extract', False, (0, 0, 0))
        transform_text = font.render('Transform', False, (0, 0, 0))
        load_text = font.render('Load Database', False, (0, 0, 0))
        extract = pg.Rect(250, 50, 300, 150)
        transform = pg.Rect(250, 300, 300, 150)
        load = pg.Rect(250, 550, 300, 150)

        SCREEN = pg.display.set_mode((800, 800))
        SCREEN.fill((255, 255, 255))
        pg.draw.rect(SCREEN, (0, 0, 0, 0), extract, 2)
        pg.draw.rect(SCREEN, (0, 0, 0, 0), transform, 2)
        pg.draw.rect(SCREEN, (0, 0, 0, 0), load, 2)
        SCREEN.blit(extract_text, (345, 100))
        SCREEN.blit(transform_text, (315, 350))
        SCREEN.blit(load_text, (285, 600))