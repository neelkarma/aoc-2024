from common import Direction, find_perims, find_regions, read_input


def count_sides(perim: set[tuple[int, int, Direction]]):
    count = 0

    # find border bounding box
    min_x = min(x for x, _, _ in perim)
    max_x = max(x for x, _, _ in perim)
    min_y = min(y for _, y, _ in perim)
    max_y = max(y for _, y, _ in perim)

    # now, iterate through the bounding box, counting continuous edges
    # first, horizontally:
    for y in range(min_y, max_y + 1):
        on_up_side = False
        on_down_side = False
        for x in range(min_x, max_x + 1):
            match ((x, y, Direction.UP) in perim, on_up_side):
                case True, False:
                    on_up_side = True
                    count += 1
                case False, True:
                    on_up_side = False

            match ((x, y, Direction.DOWN) in perim, on_down_side):
                case True, False:
                    on_down_side = True
                    count += 1
                case False, True:
                    on_down_side = False

    # then, vertically:
    for x in range(min_x, max_x + 1):
        on_left_side = False
        on_right_side = False
        for y in range(min_y, max_y + 1):
            match ((x, y, Direction.LEFT) in perim, on_left_side):
                case True, False:
                    on_left_side = True
                    count += 1
                case False, True:
                    on_left_side = False

            match ((x, y, Direction.RIGHT) in perim, on_right_side):
                case True, False:
                    on_right_side = True
                    count += 1
                case False, True:
                    on_right_side = False

    return count


grid = read_input("input.txt")
dim = len(grid)

regions = find_regions(grid, dim)
perims = find_perims(grid, regions, dim)
sides = [count_sides(perim) for perim in perims]
answer = sum(side_count * len(region) for side_count, region in zip(sides, regions))
print(answer)
