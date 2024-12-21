import re

pat = re.compile("(mul\\((\\d{1,3}),(\\d{1,3})\\))|(do\\(\\))|(don't\\(\\))")

with open("input.txt") as f:
    memory = "".join(line.strip() for line in f)
    results = pat.findall(memory)

    mul_enabled = True
    answer = 0
    for result in results:
        if result[0] and mul_enabled:
            answer += int(result[1]) * int(result[2])
        elif result[3]:
            mul_enabled = True
        elif result[4]:
            mul_enabled = False

    print(answer)
