class Map:
    CHUNK_SIZE = 256
    MAP_SIZE = 3

    def __init__(self):
        self._chunks = {}
