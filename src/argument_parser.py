"""Parses user input given in command line at runtime or list provided as an argument."""
import argparse


class ArgumentParser:
    def __init__(self, list_of_args: list = None):
        self._parser = argparse.ArgumentParser(prog="PROG", prefix_chars="-/")
        self._add_arguments()
        self._list_of_args = list_of_args
        self.args = self._parse_arguments()

    def _add_arguments(self):
        self._parser.add_argument(
            "-i",
            "--input",
            dest="filepath",
            required=True,
            metavar="FILE",
            help="path to input file",
        )

    def _parse_arguments(self):
        if self._list_of_args:
            return self._parser.parse_args(self._list_of_args)
        return self._parser.parse_args()  # using sys.argv
