"""AoC 3, 2022: Rucksack Reorganization."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    sacks = []
    for sack in data.split("\n"):
        n = len(sack)//2
        comp1 = "".join(set(sack[:n]))
        comp2 = "".join(set(sack[n:]))
        for char in comp1:
            if char in comp2 and ord(char) <= ord("Z"):
                sacks.append(ord(char) - 38)
            elif char in comp2 and ord(char) > ord("Z"):
                sacks.append(ord(char) - 96)
    return sum(sacks)


def part2(data):
    """Solve part 2."""
    sacks = []
    for sack in data.split("\n"):
        n = len(sack)//2
        comp1 = "".join(set(sack[:n]))
        comp2 = "".join(set(sack[n:]))
        for char in comp1:
            if char in comp2 and ord(char) <= ord("Z"):
                sacks.append(ord(char) - 38)
            elif char in comp2 and ord(char) > ord("Z"):
                sacks.append(ord(char) - 96)
    return sum(sacks)

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
