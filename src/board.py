"""
Represents the board

All spaces are initialized with a value of 1, representing that there is 1 coin in each space.
Walls are placed with a value of -1, representing that the space is unavailable.
When pacman, moves over a space with a coin, the coin is removed.
Any coins removed after pacman is initially placed are collected for pacman's 'score'.
"""
from typing import Tuple, List

from src.config_manager import ConfigManager
from src.move import Move


class Board:
    def __init__(self, config: ConfigManager):
        self._config = config
        self.number_of_coins_collected = 0

        self._last_row = self._config.board_height - 1

        self._wall_value = -1
        self._coin_value = 1

        self._grid = [
            [self._coin_value for _ in range(self._config.board_width)]
            for __ in range(self._config.board_height)
        ]
        self._add_walls(self._config.walls)

        self._pacman_position: Tuple[int, int] = self._config.initial_position
        self._set_grid_value_at_position(self._pacman_position, 0)

    def _set_grid_value_at_position(self, position: Tuple[int, int], value: int):
        if self._get_grid_value_at_position(position) == self._wall_value:
            # getting the grid value ensures that the position is in bounds
            raise ValueError("Tried to change the value at the position of a wall.")
        x_position, y_position = position[0], position[1]
        self._grid[self._last_row - y_position][x_position] = value

    def _get_grid_value_at_position(self, position: Tuple[int, int]) -> int:
        if not self._is_in_bounds(position):
            raise IndexError("Tried to get a position out of bounds")
        x_position, y_position = position[0], position[1]
        return self._grid[self._last_row - y_position][x_position]

    def _is_in_bounds(self, position):
        x_position, y_position = position[0], position[1]
        return (
            0 <= x_position < self._config.board_width
            and 0 <= y_position < self._config.board_height
        )

    def _add_walls(self, walls: List[Tuple[int, int]]):
        for wall in walls:
            self._set_grid_value_at_position(wall, self._wall_value)

    def allows(self, move: Move):
        desired_x, desired_y = (
            self.pacman_x + move.x_position,
            self.pacman_y + move.y_position,
        )
        if not self._is_in_bounds((desired_x, desired_y)):
            return False
        return self._get_grid_value_at_position((desired_x, desired_y)) >= 0

    def make_move(self, move: Move):
        """Set pacman's new position and collect a coin, if possible."""
        self._pacman_position = (
            self.pacman_x + move.x_position,
            self.pacman_y + move.y_position,
        )
        if self._get_grid_value_at_position(self._pacman_position) > 0:
            self.number_of_coins_collected += 1
            self._set_grid_value_at_position(self._pacman_position, 0)

    @property
    def pacman_x(self):
        return self._pacman_position[0]

    @property
    def pacman_y(self):
        return self._pacman_position[1]
