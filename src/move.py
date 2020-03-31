"""Represents x and y coordinates from a given string, which it validates."""
from dataclasses import dataclass

from typing import Dict, Tuple


@dataclass(init=False)
class Move:
    def __init__(self, direction: str):
        self._direction: str = direction
        self._cardinal_direction_to_x_y: Dict[str, Tuple[int, int]] = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }
        if self._direction not in self._cardinal_direction_to_x_y.keys():
            raise ValueError("Illegal direction provided for a Move.")

    @property
    def x_position(self):
        return self._cardinal_direction_to_x_y.get(self._direction.upper())[0]

    @property
    def y_position(self):
        return self._cardinal_direction_to_x_y.get(self._direction.upper())[1]
