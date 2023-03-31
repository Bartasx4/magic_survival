#  from magicS.engine import Engine
#  from magicS.model.player import Player


def circle(radius):
    import math
    import random

    random.seed()
    t = 2 * math.pi * random.random()
    u = random.random() + random.random()
    r = 2 - u if u > 1 else u
    return radius * r * math.cos(t), radius * r * math.sin(t)


if __name__ == '__main__':
    # engine = Engine()
    print(circle(500))
