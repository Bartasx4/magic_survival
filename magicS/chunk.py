import pygame
from typing import List

from .settings import Settings


class Chunk:
    _mobs: List
    _items: List
    _size: tuple[int, int]
    _x: int
    _y: int
    _image: pygame.Surface
    _surface: pygame.Surface
    _rect: pygame.Rect

    def __init__(self,
                 chunk_size: tuple[int, int],
                 x: int = 0,
                 y: int = 0,
                 image_size: tuple[int, int] | None = None,
                 image_repeat: bool = True):
        self._size = chunk_size
        self._x = x
        self._y = y
        self._image = pygame.image.load('magicS/sprites/ground.png')
        self._image = pygame.transform.scale(self._image, image_size) if image_size else self._image
        self._surface = pygame.Surface(self._size)
        self.__repeat() if image_repeat else self.__stretch()
        self._rect = self._surface.get_rect()

    @property
    def surface(self):
        return self._surface

    @property
    def rect(self):
        return self._rect

    @property
    def to_coord(self):
        return self._x * self._size[0], self._y * self._size[1]

    def __repeat(self, set_size=None):
        if set_size is not None:
            image = pygame.transform.scale(self._image, (set_size, set_size))
        else:
            image = self._image
        image_size = image.get_size()
        for x in range(0, self._size[0], image_size[0]):
            for y in range(0, self._size[1], image_size[1]):
                self._surface.blit(image, (x, y))

    def __stretch(self):
        image = pygame.transform.scale(self._image, self._size)
        self._surface.blit(image, self._surface.get_rect())
