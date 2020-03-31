"""Parses a file from text to a list, where each entry in the list is a line from the file."""
from typing import List


class FileParser:
    @staticmethod
    def parse(path_to_file: str) -> List[str]:
        with open(path_to_file, "r") as file:
            lines = file.readlines()
        return [line.strip() for line in lines]
