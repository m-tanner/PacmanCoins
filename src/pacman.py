"""Uses input from a text file to create a board and move 'pacman' on it, collecting coins."""
from typing import List

from src.board import Board
from src.config_manager import ConfigManager
from src.file_parser import FileParser

__author__ = "Michael Tanner"
__email__ = "tanner.mbt@gmail.com"


def pacman(input_file):
    """
    Input:
        1. input_file (String) =
            contains the name of a text file you need to read that is in the same directory,
            includes the ".txt" extension (ie. "input.txt")
    Outputs:
        1. final_pos_x (int) = final x location of Pacman
        2. final_pos_y (int) = final y location of Pacman
        3. coins_collected (int) =
            the number of coins that have been collected by Pacman across all movements
    """
    try:
        lines_of_file: List[str] = FileParser().parse(path_to_file=input_file)
        config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)
        board: Board = Board(config=config_manager)
        for move in config_manager.moves:
            if board.allows(move):
                board.make_move(move)
        return (
            board.pacman_x,
            board.pacman_y,
            board.number_of_coins_collected,
        )
    except (IndexError, ValueError):
        return -1, -1, 0
