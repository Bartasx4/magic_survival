import pygame
from pygame.locals import *

from .chunk import Chunk

pygame.init()


class Engine:

    def __init__(self):
        self._running = True
        self._clock = pygame.time.Clock()
        self._window = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Magic survival')
        self.__loop()

    def __get_event(self):
        mouse = pygame.mouse
        for event in pygame.event.get():
            if self.__is_exit_event(event):
                return
            if mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
            # if event.type ==

    def __is_exit_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self._running = False
        elif event.type == QUIT:
            self._running = False
        return False if self._running else True

    def __loop(self):
        chunk = Chunk((600, 600))
        while self._running:
            self._clock.tick(60)
            self.__get_event()
            self._window.fill('white')
            self._window.blit(chunk.surface, chunk.rect)
            self.__draw_dev_menu()
            pygame.display.update()

    def __draw_dev_menu(self):
        font = pygame.font.Font(None, 32)
        fps_text = font.render(str(int(self._clock.get_fps())), True, (50, 200, 20))
        fps_rect = fps_text.get_rect()
        fps_rect.x += 15
        fps_rect.y += 15
        self._window.blit(fps_text, fps_rect)
