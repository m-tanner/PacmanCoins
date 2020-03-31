import os
import unittest
from typing import List

from src.config_manager import ConfigManager
from src.file_parser import FileParser


class AllTests(unittest.TestCase):
    def test_board_input_too_small(self):
        lines_of_file: List[str] = FileParser().parse(
            path_to_file=os.path.join("tests", "resources", "board_input_too_small.txt")
        )
        with self.assertRaises(ValueError):
            config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)

    def test_board_input_too_big(self):
        lines_of_file: List[str] = FileParser().parse(
            path_to_file=os.path.join("tests", "resources", "board_input_too_big.txt")
        )
        with self.assertRaises(ValueError):
            config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)

    def test_pacman_input_too_small(self):
        lines_of_file: List[str] = FileParser().parse(
            path_to_file=os.path.join(
                "tests", "resources", "pacman_input_too_small.txt"
            )
        )
        with self.assertRaises(ValueError):
            config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)

    def test_pacman_input_too_big(self):
        lines_of_file: List[str] = FileParser().parse(
            path_to_file=os.path.join("tests", "resources", "pacman_input_too_big.txt")
        )
        with self.assertRaises(ValueError):
            config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)

    def test_move_input_too_small(self):
        lines_of_file: List[str] = FileParser().parse(
            path_to_file=os.path.join("tests", "resources", "move_input_too_small.txt")
        )
        with self.assertRaises(ValueError):
            config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)

    def test_wall_input_too_small(self):
        lines_of_file: List[str] = FileParser().parse(
            path_to_file=os.path.join("tests", "resources", "wall_input_too_small.txt")
        )
        with self.assertRaises(ValueError):
            config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)

    def test_wall_input_too_big(self):
        lines_of_file: List[str] = FileParser().parse(
            path_to_file=os.path.join("tests", "resources", "wall_input_too_big.txt")
        )
        with self.assertRaises(ValueError):
            config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)

    def test_input_that_has_commas(self):
        lines_of_file: List[str] = FileParser().parse(
            path_to_file=os.path.join("tests", "resources", "bad_commas.txt")
        )
        with self.assertRaises(ValueError):
            config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)

    def test_bad_directions(self):
        lines_of_file: List[str] = FileParser().parse(
            path_to_file=os.path.join("tests", "resources", "bad_directions.txt")
        )
        with self.assertRaises(ValueError):
            config_manager: ConfigManager = ConfigManager(inputs=lines_of_file)


if __name__ == "__main__":
    for testClass in [AllTests]:
        print("\n\nTest Class: {}\n".format(testClass.__name__))
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        result = unittest.TextTestRunner(verbosity=0).run(suite)
