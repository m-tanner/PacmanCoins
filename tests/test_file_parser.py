import os
import unittest

from src.file_parser import FileParser


class AllTests(unittest.TestCase):
    def test_empty(self):
        lines = FileParser().parse(os.path.join("tests", "resources", "empty.txt"))
        expected = []
        self.assertEqual(type(lines), list)
        self.assertEqual(lines, expected)

    def test_one_line(self):
        lines = FileParser().parse(os.path.join("tests", "resources", "one_line.txt"))
        self.assertEqual(type(lines), list)
        self.assertEqual(len(lines), 1)
        self.assertEqual(lines, ["1line"])

    def test_two_line(self):
        lines = FileParser().parse(os.path.join("tests", "resources", "two_lines.txt"))
        self.assertEqual(type(lines), list)
        self.assertEqual(len(lines), 2)
        self.assertEqual(lines, ["1line", "2line"])

    def test_three_line(self):
        lines = FileParser().parse(
            os.path.join("tests", "resources", "three_lines.txt")
        )
        self.assertEqual(type(lines), list)
        self.assertEqual(len(lines), 3)
        self.assertEqual(lines, ["1line", "2line", "3line"])

    def test_four_line(self):
        lines = FileParser().parse(os.path.join("tests", "resources", "four_lines.txt"))
        self.assertEqual(type(lines), list)
        self.assertEqual(len(lines), 4)
        self.assertEqual(lines, ["1line", "2line", "3line", "4line"])

    def test_with_lines(self):
        lines = FileParser().parse(os.path.join("tests", "resources", "generic.txt"))
        expected = [
            "10 10",
            "1 5",
            "NNNESENNWESESSWSSENNENNEEEESESSWWSWSESS",
            "1 7",
            "1 8",
            "2 5",
            "3 4",
            "3 5",
            "3 6",
            "3 7",
            "5 6",
            "5 7",
            "7 3",
            "8 4",
            "9 4",
        ]
        self.assertEqual(type(lines), list)
        self.assertEqual(lines, expected)


if __name__ == "__main__":
    for testClass in [AllTests]:
        print("\n\nTest Class: {}\n".format(testClass.__name__))
        suite = unittest.TestLoader().loadTestsFromTestCase(testClass)
        result = unittest.TextTestRunner(verbosity=0).run(suite)
