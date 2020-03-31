[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# PacmanCoins

## Requirements

### Example Input
This program takes as input the name of a text file (ie. "input.txt"), which contains the following inputs:

1. `board_dimension` is given on the first line. It is defined by [X and Y coordinates](https://en.wikipedia.org/wiki/Cartesian_coordinate_system), identifying the top right corner of the room rectangle - that is to say, (0,0) is in the bottom left corner, and (X,Y) is in the top right corner. This board is divided up in a grid based on these dimensions; a board that has dimensions `X=5` and `Y=5` has 5 columns and 5 rows for 25 possible positions.
2. `initial_position` is given on the second line. It is the initial position of Pac-Man in (x,y) coordinates.
3. `movements` are given on the third line. They are instructions in [cardinal directions](https://en.wikipedia.org/wiki/Cardinal_direction) where e.g. N and E mean "go north" and "go east", respectively. The board is oriented facing north; thus, moving north from (0,0) lands Pac-Man at (0,1).
4. `walls` are given on the remaining lines. They are the positions of walls on the board in (x,y) coordinates. Pac-Man cannot move through walls.

For an input file to be valid, it must contain a `board_dimension`, an `initial_position` and at least one movement in `movements`.

Example input values:
```
5 5
1 2
NNESEESWNWW
1 0
2 2
2 3
```

This input would tell the program that there is a 5 x 5 board with walls placed at positions `[(1,0),(2,2),(2,3)]`. Pac-Man would start at position `(1,2)` and will "attempt" to move in the following sequence: `N-N-E-S-E-E-S-W-N-W-W`.

### Example Output
Given the inputs described above, the program would have two outputs:

- Pac-Man's final location in (x,y)
- The number of coins that have been collected across all movements

Matching the input above, the function would return something like:  
```py
# finalXposition, finalYposition, totalCoins
return (1, 4, 7)
```

## Documentation

I have attempted to write self-documenting code or write docstrings and comments as necessary. 

## Setup
Create a new virtual Python environment. This example uses conda, but feel free to use that with which you're familiar.

This code does make use of a Python 3.8 feature in 'main.py'.
```
conda create -n pacman python=3.8
conda activate pacman
```

Install the code and its requirements
```
# Ensure you are in the project's root directory (where the setup.py file is)
cd pacman-master/

# Install the project and its dependencies into the active Python environment
pip install .

# If you want to run the tests, be sure to install the dependencies
pip install ".[tests]"

# Or if you'd like to install in editable mode and develop further
pip install -e .
# Or
pip install -e ".[tests]"
```

## Run
```
# Ensure you are in the Python environment where the project and its dependencies were installed
# If you followed the example above and used conda
conda activate pacman

# Run the script
pacman -i resources/input.txt
```

## Test
```
# Ensure you are in the Python environment where the project and its dependencies were installed
# If you followed the example above and used conda
conda activate pacman

# Ensure you are in the root directory of the project
cd pacman-master/

# Run the tests with coverage
coverage run --source=src/ -m unittest discover -v -b
# -v will show the name of each test
# -b will suppress output unless a test fails

# To view the coverage
coverage report --omit="*main*" -m
# -m will show exactly which lines are missing coverage, if any

# Or without coverage
python -m unittest discover -v -b

# To test for formatting
black . --check

# To test for static failures
pylint src/ --errors-only
```

It's also possible to run the tests from any particular test file by running the file as a script.
```
# For instance
cd pacman-master/
python tests/test_pacman.py
```
