# using the decompiled output from decompiler.py
def run():
    out = []
    a = 24847151
    b = 0
    c = 0

    while a != 0:
        b = a % 8
        b = b ^ 5
        c = a >> b
        b = b ^ 6
        a = a >> 3
        b = b ^ c
        out.append(b % 8)

    return out


print(",".join(map(str, run())))
