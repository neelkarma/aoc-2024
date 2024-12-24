import re

given = re.compile(r"(x|y)\d{2}")

instrs = []


with open("input.txt") as f:
    _, instrs_part = f.read().split("\n\n")
    instrs = instrs_part.splitlines()

seen = set()
for i in range(46):
    n = f"{i:02}"

    xor_instr = None
    and_instr = None
    xor_target = None
    and_target = None

    for instr in instrs:
        a, x, b, _, t = instr.split()
        if a == "x" + n or b == "x" + n or a == "y" + n or b == "y" + n:
            print(instr)
            seen.add(instr)
            if x == "AND":
                and_instr = instr
                and_target = t
            elif x == "XOR":
                xor_instr = instr
                xor_target = t

    if xor_target is None or and_target is None:
        print("warning: no xor or and target found")
        continue

    for instr in instrs:
        a, x, b, _, t = instr.split()
        if a == xor_target or b == xor_target or a == and_target or b == and_target:
            seen.add(instr)
            print(instr)

    print("")

for instr in instrs:
    if instr not in seen:
        print(instr)
