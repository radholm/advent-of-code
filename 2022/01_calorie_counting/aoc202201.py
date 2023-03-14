"""AoC 1, 2022: calorie_counting."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    cal = []
    curRes = 0
    for line in data.split('\n'):
        if line == '':
            cal.append(curRes)
            curRes = 0
        else: curRes += int(line)
    cal.sort(reverse = True)
    return cal


def part2(data):
    """Solve part 2."""
    return sum(part1(data)[0:3])


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)[0]
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
