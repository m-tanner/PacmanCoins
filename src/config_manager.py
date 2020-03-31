"""Represents and validates user input needed to play 'pacman'."""
from typing import List, Tuple

from src.move import Move


class ConfigManager:
    def __init__(self, inputs: List[str]):
        if len(inputs) < 3:
            raise ValueError(
                f"Not enough entry inputs provided when initializing {type(self).__name__}."
            )

        self._board_size = self._string_to_int_tuple(inputs[0])
        if len(self._board_size) != 2:
            raise ValueError(
                f"{len(self._board_size)} arguments provided for board size. Needed 2."
            )
        self.board_width = self._board_size[0]
        self.board_height = self._board_size[1]

        self.initial_position = self._string_to_int_tuple(inputs[1])
        if len(self.initial_position) != 2:
            raise ValueError(
                f"{len(self.initial_position)} arguments provided for initial position. Needed 2."
            )

        self.moves = self._determine_moves(inputs[2])
        if len(self.moves) < 1:
            raise ValueError(
                f"{len(self.moves)} arguments provided for moves. Needed at least 1."
            )

        self.walls = []
        if len(inputs) > 3:
            self.walls = self._determine_walls(inputs[3:])

    @staticmethod
    def _string_to_int_tuple(string: str) -> Tuple[int, ...]:
        return tuple([int(something) for something in string.split(" ")])

    @staticmethod
    def _determine_moves(moves: str) -> List[Move]:
        return [Move(move) for move in moves]

    def _determine_walls(self, walls: List[str]) -> set:
        result: set = set()
        for desired_wall in walls:
            new_wall: Tuple[int, ...] = self._string_to_int_tuple(desired_wall)
            if len(new_wall) != 2:
                raise ValueError(
                    f"{len(new_wall)} arguments provided for a wall. Needed 2."
                )
            result.add(new_wall)
        return result
