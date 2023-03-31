
class Settings:
    CHUNK_SIZE = (600, 600)
    CHUNK_IMAGE_REPEAT = True
    CHUNK_IMAGE_SIZE = 512

    MAP_SIZE = (10, 10)  # in chunks

    DEV_MENU = True

    class Chunk:
        size = (600, 600)
        image_repeat = True
        image_size = 512

    class Map:
        size = (10, 10)  # in chunks
        visibility_range = (600, 600)  # chunk size
