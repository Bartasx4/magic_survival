from .settings import Settings
from .model.player import Player


class Map:

    def __init__(self, player: Player):
        self._chunks = {}

    def draw(self, x_range, y_range):
        ...
