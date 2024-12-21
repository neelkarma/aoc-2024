# 1. parse the file
rules = {}
manuals = []
with open("input.txt") as f:
    rules_part, manuals_part = f.read().split("\n\n")

    for line in rules_part.split("\n"):
        before, after = map(int, line.split("|"))
        if before in rules:
            rules[before].append(after)
        else:
            rules[before] = [after]

    for line in manuals_part.split("\n"):
        manual = []
        for num in line.split(","):
            if not num:
                continue
            manual.append(int(num))
        manuals.append(manual)
    manuals.pop() # we pop to ignore the final (blank) line

# 2. identify correct manuals
correct_manuals = []
for manual in manuals:
    seen = set()
    valid = True
    for num in manual:
        if num in rules:
            afters = rules[num]
            if any(after in seen for after in afters):
                valid = False
                break
        seen.add(num)

    if valid:
        correct_manuals.append(manual)

# 3. compute answer
answer = sum(manual[len(manual) // 2] for manual in correct_manuals)
print(answer)
