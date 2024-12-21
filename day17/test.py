target = [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 0, 5, 5, 3, 0]
start_a = 0

while True:
    out = []
    a = start_a
    b = 0
    c = 0

    while a != 0:
        b = a % 8  # 0
        b = b ^ 5  # 2
        c = a // (2**b)  # 4
        b = b ^ 6  # 6
        a = a // 8  # 8
        b = b ^ c  # 10
        out.append(b % 8)  # 12

        if out[-1] != target[len(out) - 1]:
            break

    start_a += 1
