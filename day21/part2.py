from common import find_total_presses, read_input

codes = read_input("input.txt")
answer = 0
for code in codes:
    presses = find_total_presses(code, 25)
    complexity = presses * int(code[:-1])
    answer += complexity

print(answer)
