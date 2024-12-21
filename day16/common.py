from collections import defaultdict
from enum import IntEnum


class Direction(IntEnum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def clockwise(self):
        return {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }[self]

    def anticlockwise(self):
        return {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH,
        }[self]

    def vector(self):
        return {
            Direction.NORTH: (0, -1),
            Direction.EAST: (1, 0),
            Direction.SOUTH: (0, 1),
            Direction.WEST: (-1, 0),
        }[self]


def read_input(fname: str):
    with open(fname) as f:
        return [line.rstrip() for line in f]


def find_start_end(grid: list[str]):
    start = None
    end = None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                start = x, y
            elif cell == "E":
                end = x, y

            if start is not None and end is not None:
                return start, end

    raise RuntimeError("start and end not found")


def make_graph(grid: list[str]):
    graph = defaultdict(dict)
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "#":
                continue

            for d in Direction:
                graph[(x, y, d)][(x, y, d.clockwise())] = 1000
                graph[(x, y, d)][(x, y, d.anticlockwise())] = 1000

                dx, dy = d.vector()
                px, py = x + dx, y + dy

                if grid[py][px] == "#":
                    continue

                graph[(x, y, d)][(px, py, d)] = 1

    graph = dict(graph)
    return graph
