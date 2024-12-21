from common import find_perims, find_regions, read_input

grid = read_input("input.txt")
dim = len(grid)

regions = find_regions(grid, dim)
perims = find_perims(grid, regions, dim)
answer = sum(len(region) * len(perim) for region, perim in zip(regions, perims))
print(answer)
