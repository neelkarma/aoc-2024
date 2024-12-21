from collections import deque
from enum import Enum


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


def read_input(fname: str) -> list[str]:
    with open(fname) as f:
        return [line.rstrip() for line in f]


def find_regions(grid: list[str], dim: int) -> list[set[tuple[int, int]]]:
    visited = set()
    regions = []

    for oy, row in enumerate(grid):
        for ox, char in enumerate(row):
            if (ox, oy) in visited:
                continue
            region = {
                (ox, oy),
            }
            queue = deque([(ox, oy)])
            while queue:
                x, y = queue.popleft()

                for px, py in [
                    (x + 1, y),
                    (x, y + 1),
                    (x - 1, y),
                    (x, y - 1),
                ]:
                    if not (0 <= px < dim and 0 <= py < dim):
                        continue
                    if (px, py) in visited or grid[py][px] != char:
                        continue
                    queue.append((px, py))
                    region.add((px, py))
                    visited.add((px, py))
            regions.append(region)

    return regions


def find_perims(
    grid: list[str], regions: list[set[tuple[int, int]]], dim: int
) -> list[set[tuple[int, int, Direction]]]:
    perims = [set() for _ in range(len(regions))]

    # first, trace the edges of the grid
    for x in range(dim):
        for i, region in enumerate(regions):
            if (x, 0) in region:
                perims[i].add((x, 0, Direction.UP))
            if (x, dim - 1) in region:
                perims[i].add((x, dim, Direction.DOWN))

    for y in range(dim):
        for i, region in enumerate(regions):
            if (0, y) in region:
                perims[i].add((0, y, Direction.LEFT))
            if (dim - 1, y) in region:
                perims[i].add((dim, y, Direction.RIGHT))

    # then, iterate through the grid, looking for borders (that is, differing adjacent cells)
    # first, horizontally:
    for y in range(dim):
        for x in range(dim - 1):
            left = grid[y][x]
            right = grid[y][x + 1]

            if left == right:
                continue

            for i, region in enumerate(regions):
                if (x, y) in region:
                    perims[i].add((x + 1, y, Direction.RIGHT))
                elif (x + 1, y) in region:
                    perims[i].add((x + 1, y, Direction.LEFT))

    # then, vertically:
    for x in range(dim):
        for y in range(dim - 1):
            top = grid[y][x]
            bottom = grid[y + 1][x]

            if top == bottom:
                continue

            for i, region in enumerate(regions):
                if (x, y) in region:
                    perims[i].add((x, y + 1, Direction.DOWN))
                elif (x, y + 1) in region:
                    perims[i].add((x, y + 1, Direction.UP))

    return perims
