input = []

with open("example.txt") as f:
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

i = 0
while True:
    end = None
    try:
        while end is None:
            end = filesystem.pop()

        i = filesystem.index(None, i)
        filesystem[i] = end

    except ValueError:
        filesystem.append(end)
        break

answer = sum(pos * i for pos, i in enumerate(filesystem))
print(answer)
