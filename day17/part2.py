program = [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 0, 5, 5, 3, 0]


def run(start_a):
    out = []
    a = start_a
    b = 0
    c = 0

    while a != 0:
        b = a % 8  # 0
        b = b ^ 5  # 2
        c = a >> b  # 4
        b = b ^ 6  # 6
        a = a >> 3  # 8
        b = b ^ c  # 10
        out.append(b % 8)  # 12

    return out


# courtesy of https://www.reddit.com/r/adventofcode/comments/1hg38ah/comment/m2gliho
# this was easily the hardest problem yet


def find(a, i):
    if run(a) == program:
        print(a)
    if run(a) == program[-i:] or not i:
        for n in range(8):
            find(8 * a + n, i + 1)


find(0, 0)
