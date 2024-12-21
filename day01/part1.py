l1 = []
l2 = []

with open("input.txt") as f:
    for line in f:
        num1, num2 = map(int, line.rstrip().split())
        l1.append(num1)
        l2.append(num2)

l1.sort()
l2.sort()

total = sum(abs(num1 - num2) for num1, num2 in zip(l1, l2))
print(total)
