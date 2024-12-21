from common import find_dists, generate_cheat_times, read_input

walls, xi, yi, xf, yf, dim = read_input("input.txt")
dists_from_start = find_dists((xi, yi), walls)
dists_from_end = find_dists((xf, yf), walls)
fastest_time = dists_from_start[(xf, yf)]

answer = sum(
    fastest_time - time >= 100
    for time in generate_cheat_times(20, dists_from_start, dists_from_end, walls, dim)
)
print(answer)
