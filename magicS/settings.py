from .chunk import Chunk
from .map import Map


class Settings:
    CHUNK_SIZE = (600, 600)
    CHUNK_IMAGE_REPEAT = True
    CHUNK_IMAGE_SIZE = 512

    MAP_SIZE = (10, 10)  # in chunks

    def __new__(cls, *args, **kwargs):
        if Chunk in args:
            return cls.chunk(cls)
        if Map in args:
            return cls.map(cls)

    @staticmethod
    def chunk(cls):

        class ChunkSettings:
            size = cls.CHUNK_SIZE
            image_repeat = cls.CHUNK_IMAGE_REPEAT
            image_size = cls.CHUNK_IMAGE_SIZE
        return ChunkSettings()

    @staticmethod
    def map(cls):

        class MapSettings:
            size = cls.MAP_SIZE
        return MapSettings()

