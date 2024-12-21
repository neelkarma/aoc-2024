answer = 0
progress = 0

with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        test, operands = line.split(": ")
        test = int(test)
        operands = [int(num) for num in operands.split()]

        # fuck it, we ball

        # 0 for +, 1 for *, 2 for ||
        ops = [0 for _ in range(len(operands) - 1)]
        i = 0
        while i < 3 ** len(ops):
            acc = operands[0]
            for j in range(len(ops)):
                op = ops[j]
                if op == 0:
                    acc += operands[j + 1]
                elif op == 1:
                    acc *= operands[j + 1]
                elif op == 2:
                    acc = int(str(acc) + str(operands[j + 1]))
                if acc > test:
                    break
            if acc == test:
                answer += test
                break

            for j in range(len(ops)):
                ops[j] += 1
                if ops[j] >= 3:
                    ops[j] -= 3
                else:
                    break

            i += 1
        progress += 1
        print(progress)

print(answer)
