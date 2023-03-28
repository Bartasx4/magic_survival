class Model:
    _attack: float
    _defence: float
    _direction: int
    _exp: float
    _hp: int
    _name: str
    _position: tuple[int, int]
    _size: float
    _velocity: float

    def __init__(self, attack: float,
                 defence: float,
                 direction: int,
                 exp: float,
                 hp: int,
                 name: str,
                 position: tuple[int, int],
                 size: float,
                 velocity: float):
        self._attack = attack
        self._defence = defence
        self._direction = direction
        self._exp = exp
        self._hp = hp
        self._name = name
        self._position = position
        self._size = size
        self._velocity = velocity
