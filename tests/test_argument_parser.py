import sys
from unittest import TestCase, TestLoader, TextTestRunner
from unittest.mock import patch

from src.argument_parser import ArgumentParser


class AllTests(TestCase):
    @patch("sys.argv", ["-i", "filepath"])
    def test_successful_parsing(self):
        args_to_test = [
            sys.argv,
            ["-i", "filepath"],
        ]
        for args in args_to_test:
            parser = ArgumentParser(list_of_args=args)
            self.assertNotEqual(parser.args, None)

    def test_failing_to_parse(self):
        args_to_test = [sys.argv, [], [""], ["-i"]]
        for args in args_to_test:
            with self.assertRaises(SystemExit):
                ArgumentParser(list_of_args=args)


if __name__ == "__main__":
    for testClass in [AllTests]:
        print("\n\nTest Class: {}\n".format(testClass.__name__))
        suite = TestLoader().loadTestsFromTestCase(testClass)
        result = TextTestRunner(verbosity=0).run(suite)
