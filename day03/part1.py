import re

pat = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)")

with open("input.txt") as f:
    memory = "".join(line.strip() for line in f)
    results = pat.findall(memory)
    answer = sum(int(n1) * int(n2) for n1, n2 in results)
    print(answer)
