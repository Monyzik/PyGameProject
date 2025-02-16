from os import PathLike

import pygame.image


class Animation:
    def __init__(self, animation_path: str, count_of_columns: int, count_of_rows: int):
        self.animation_path = animation_path
        self.count_of_rows = count_of_rows
        self.count_of_columns = count_of_columns

    def get_surface(self) -> pygame.Surface:
        return pygame.image.load(self.animation_path)

    def get_size(self) -> list[int]:
        return [self.count_of_columns, self.count_of_rows]
