def viz(filesystem, i, j):
    print("".join(str(n) if n is not None else "." for n in filesystem))
    print(" " * i + "i")
    print(" " * j + "j")
    print("")

input = []

with open("input.txt") as f:
    input = list(map(int, f.readline().rstrip()))

filesystem = []
i = 0
reading_frees = False
for num in input:
    if reading_frees:
        filesystem += [None] * num
        reading_frees = False
        continue

    filesystem += [i] * num
    i += 1
    reading_frees = True


i = len(filesystem) - 1
while i >= 0:
    # find the size of the current file
    while filesystem[i] is None:
        i -= 1
    end = i
    while filesystem[i] == filesystem[end]:
        i -= 1
    start = i + 1
    filesize = end - start + 1

    # find any space that can fit the file
    space = 0
    space_start = 0
    j = 0
    while space < filesize:
        while filesystem[j] is not None:
            j += 1
        if j > i:
            break
        space_start = j
        while filesystem[j] is None:
            j += 1
        space_end = j - 1
        space = space_end - space_start + 1

    # if space is sufficient, move
    if space >= filesize:
        for n in range(filesize):
            filesystem[space_start + n] = filesystem[start + n]
            filesystem[start + n] = None

answer = sum(pos * n for pos, n in enumerate(filesystem) if n is not None)
print(answer)
