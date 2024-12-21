# credit to https://github.com/xhyrom/aoc/blob/main/2024/21/solution.py and a reddit comment i can't find anymore for improving my existing (terrible) solution

from functools import cache
from itertools import permutations

NUM_PAD = ["789", "456", "123", " 0A"]
DIR_PAD = [" ^A", "<v>"]


def gen_coords(pad):
    coords = {}
    for y, row in enumerate(pad):
        for x, cell in enumerate(row):
            if cell != " ":
                coords[cell] = x, y
    return coords


num_coords = gen_coords(NUM_PAD)
dir_coords = gen_coords(DIR_PAD)


def path_valid(start, path, coords):
    x, y = start

    if (x, y) not in coords.values():
        return False

    for d in path:
        match d:
            case ">":
                x += 1
            case "v":
                y += 1
            case "<":
                x -= 1
            case "^":
                y -= 1

        if (x, y) not in coords.values():
            return False

    return True


def find_paths(start, end, coords):
    path = []

    xi, yi = coords[start]
    xf, yf = coords[end]
    dx = xf - xi
    dy = yf - yi

    if dx < 0:
        path.append("<" * -dx)
    else:
        path.append(">" * dx)

    if dy < 0:
        path.append("^" * -dy)
    else:
        path.append("v" * dy)

    path = "".join(path)

    seen = set()
    for p in permutations(path):
        if path_valid((xi, yi), p, coords) and p not in seen:
            p = "".join(p) + "A"
            yield p
            seen.add(p)


@cache
def find_dir_presses(sequence, depth):
    if depth == 0:
        return len(sequence)

    total = 0
    cell = "A"

    for digit in sequence:
        total += min(
            find_dir_presses(p, depth - 1) for p in find_paths(cell, digit, dir_coords)
        )

        cell = digit

    return total


def find_total_presses(code, depth):
    cell = "A"
    total = 0

    for digit in code:
        total += min(
            find_dir_presses(path, depth)
            for path in find_paths(cell, digit, num_coords)
        )
        cell = digit

    return total


def read_input(fname):
    with open(fname) as f:
        return [line.rstrip() for line in f]
