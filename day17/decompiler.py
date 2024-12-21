import sys

fname = sys.argv[1]
a, b, c = -1, -1, -1
program = []

with open(fname) as f:
    a = int(f.readline().rstrip().split(": ")[1])
    b = int(f.readline().rstrip().split(": ")[1])
    c = int(f.readline().rstrip().split(": ")[1])
    f.readline()
    program = [int(n) for n in f.readline().rstrip().split(": ")[1].split(",")]


def combo(operand: int):
    match operand:
        case _ if 0 <= operand <= 3:
            return str(operand)
        case 4:
            return "a"
        case 5:
            return "b"
        case 6:
            return "c"
    raise RuntimeError(f"invalid combo operand {operand}")


with open(f"{fname}-decompiled.py", "w+") as f:
    f.write(f"a = {a}\nb = {b}\nc = {c}\n\n")

    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i + 1]

        match opcode:
            case 0:
                f.write(f"a = a >> {combo(operand)}")
            case 1:
                f.write(f"b = b ^ {operand}")
            case 2:
                f.write(f"b = {combo(operand)} % 8")
            case 3:
                f.write(f"if a != 0: pass # jump to {operand}")
            case 4:
                f.write("b = b ^ c")
            case 5:
                f.write(f"print({combo(operand)} % 8)")
            case 6:
                f.write(f"b = a >> {combo(operand)}")
            case 7:
                f.write(f"c = a >> {combo(operand)}")

        f.write(f"  # {i}\n")

        i += 2
