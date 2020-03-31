"""A script to play 'pacman'."""
from src.argument_parser import ArgumentParser
from src.pacman import pacman


def main():
    argument_parser = ArgumentParser()
    final_x_position, final_y_position, coins = pacman(argument_parser.args.filepath)
    print(f"{final_x_position=}, {final_y_position=}, {coins=}")


if __name__ == "__main__":
    main()
