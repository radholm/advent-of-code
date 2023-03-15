# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    scoreTable = {"A": {"X": 4, "Y": 8, "Z": 3},
                  "B": {"X": 1, "Y": 5, "Z": 9},
                  "C": {"X": 7, "Y": 2, "Z": 6}}
    return sum(scoreTable[turn[0]][turn[-1]] for turn in data.split("\n"))


def part2(data):
    """Solve part 2."""
    turnTable = {"A": {"Y": 4, "Z": 8, "X": 3},
                 "B": {"X": 1, "Y": 5, "Z": 9},
                 "C": {"Z": 7, "X": 2, "Y": 6}}
    return sum(turnTable[turn[0]][turn[-1]] for turn in data.split("\n"))


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
