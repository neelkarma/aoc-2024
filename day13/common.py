import re

a_pat = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
b_pat = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
t_pat = re.compile(r"Prize: X=(\d+), Y=(\d+)")


def read_input(fname: str, part2=False):
    correction = 10000000000000 if part2 else 0
    with open(fname) as f:
        input = f.read()
        return [
            (
                int(ax),
                int(ay),
                int(bx),
                int(by),
                int(tx) + correction,
                int(ty) + correction,
            )
            for (ax, ay), (bx, by), (tx, ty) in zip(
                a_pat.findall(input), b_pat.findall(input), t_pat.findall(input)
            )
        ]


def calc_tokens(ax: int, ay: int, bx: int, by: int, tx: int, ty: int):
    # math™
    a = (by * tx - bx * ty) / (ax * by - bx * ay)
    b = (ay * tx - ax * ty) / (ay * bx - by * ax)

    if a.is_integer() and b.is_integer():
        return 3 * int(a) + int(b)
    else:
        return 0
