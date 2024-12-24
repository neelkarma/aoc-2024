"""
FIRST ADDITION
--------------
x00 AND y00 -> car
x00 XOR y00 -> z00

SUBSEQUENT ADDITIONS
--------------------
xxx XOR yyy -> t01
xxx AND yyy -> t02
t01 XOR car -> zzz
t01 AND car -> t03
t02 OR t03 -> car
"""

instrs = []
with open("input.txt") as f:
    _, instrs = f.read().split("\n\n")
    instrs = instrs.splitlines()

carry = "gwq"

for i in range(1, 45):
    x = f"x{i:02}"
    y = f"y{i:02}"
    z = f"z{i:02}"
    zn = f"z{i + 1:02}"

    t1 = None
    t2 = None

    for instr in instrs:
        a, x, b, _, t = instr.split()
        if a in (x, y) or b in (x, y):
            if x == "AND":
                t2 = t
            elif x == "XOR":
                t1 = t
            else:
                print(f"Anomaly (i = {i}): {instr}")

    if t1 is None or t2 is None:
        print(f"Anomaly (i = {i}): and or xor not found")
        continue

    print(t1, carry)
    t3 = None
    for instr in instrs:
        a, x, b, _, t = instr.split()

        if (a, b) == (t1, carry) or (a, b) == (carry, t1):
            if x == "XOR":
                if t != z:
                    print(f"Anomaly (i = {i}): {instr}")
            elif x == "AND":
                t3 = t

    if t3 is None:
        print(f"Anomaly (i = {i}): t03 not found")
        continue

    for instr in instrs:
        a, x, b, _, t = instr.split()
        if (a, b) == (t2, t3) or (a, b) == (t3, t2):
            if x != "OR":
                print(f"Anomaly (i = {i}): {instr}")
            carry = t
