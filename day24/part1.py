from enum import IntEnum


class Operation(IntEnum):
    AND = 0
    OR = 1
    XOR = 2

    @staticmethod
    def from_str(s):
        return {"AND": Operation.AND, "OR": Operation.OR, "XOR": Operation.XOR}[s]

    def exec(self, a, b):
        match self:
            case Operation.AND:
                return a and b
            case Operation.OR:
                return a or b
            case Operation.XOR:
                return a ^ b


values = {}
dependencies = {}

with open("input.txt") as f:
    initial_part, instrs_part = f.read().split("\n\n")

    values = {
        name: value == "1"
        for name, value in (line.split(": ") for line in initial_part.splitlines())
    }

    for line in instrs_part.splitlines():
        a, instr, b, _, out = line.split()
        dependencies[out] = a, b, Operation.from_str(instr)

while dependencies:
    for out, (a, b, op) in list(dependencies.items()):
        if a not in values or b not in values:
            continue
        values[out] = op.exec(values[a], values[b])
        dependencies.pop(out)

i = 0
answer = 0
while f"z{i:02}" in values:
    if values[f"z{i:02}"]:
        answer += 2**i
    i += 1

print(answer)
