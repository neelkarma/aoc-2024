from common import calc_tokens, read_input

machines = read_input("input.txt")
answer = sum(map(lambda machine: calc_tokens(*machine), machines))
print(answer)
