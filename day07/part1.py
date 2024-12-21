def get_bit(value, n):
    return (value >> n & 1) != 0

answer = 0
with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        test, operands = line.split(": ")
        test = int(test)
        operands = [int(num) for num in operands.split()]

        # fuck it, we ball
        i = 0
        while i < 2 ** len(operands):
            acc = operands[0]
            for j in range(1, len(operands)):
                plus = get_bit(i, j)
                if plus:
                    acc += operands[j]
                else:
                    acc *= operands[j]
            if acc == test:
                answer += test
                break
            i += 1
print(answer)
