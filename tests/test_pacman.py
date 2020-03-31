"""
Unit tests for pacman.py

Renamed from pacman.ut.py to enable unittest's test discovery
To add new tests:
1) Place new text files in the tests/resources folder
2) Add new methods here, leading each function name with "test_"
3) Run the tests per the README
   or by executing the test file as a script from the project's root directory
"""
import os
import unittest

from src.pacman import pacman


class AllTests(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "generic.txt")), (6, 1, 27)
        )

    def test_edge(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "edge.txt")), (-1, -1, 0)
        )

    def test_runtime(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "runtime.txt")), (2142, 147, 148)
        )

    def test_empty(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "empty.txt")), (-1, -1, 0)
        )

    def test_pacman_start_on_wall(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "pacman_start_on_wall.txt")),
            (-1, -1, 0),
        )

    def test_wall_outside_board(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "wall_outside_board.txt")),
            (-1, -1, 0),
        )

    def test_board_of_size_zero(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "board_of_size_zero.txt")),
            (-1, -1, 0),
        )

    def test_wall_input_zero(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "wall_input_zero.txt")),
            (7, 1, 35),
        )

    def test_from_instructions(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "from_instructions.txt")),
            (1, 4, 7),
        )

    def test_into_edges(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "into_edges.txt")), (0, 0, 15),
        )

    def test_into_wall_at_center(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "into_wall_at_center.txt")),
            (0, 0, 10),
        )

    def test_into_start(self):
        self.assertEqual(
            pacman(os.path.join("tests", "resources", "into_start.txt")), (0, 0, 1),
        )


if __name__ == "__main__":
    for testClass in [AllTests]:
        print("\n\nTest Class: {}\n".format(testClass.__name__))
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        result = unittest.TextTestRunner(verbosity=0).run(suite)
