from .model import Model


class Player(Model):

    def __init__(self, attack: float,
                 defence: float,
                 direction: int,
                 exp: float,
                 hp: int,
                 name: str,
                 position: tuple[int, int],
                 size: float,
                 velocity: float):
        super().__init__(attack, defence, direction, exp, hp, name, position, size, velocity)


