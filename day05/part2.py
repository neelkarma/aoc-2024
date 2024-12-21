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
    manuals.pop()

# 2. identify incorrect manuals
incorrect_manuals = []
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

    if not valid:
        incorrect_manuals.append(manual)

# 3. now, invert the rules such that `after` is the key
new_rules = {}
for before, afters in rules.items():
    for after in afters:
        if after in new_rules:
            new_rules[after].append(before)
        else:
            new_rules[after] = [before]
rules = new_rules

# 4. correct the incorrect manuals
corrected_manuals = []
for incorrect_manual in incorrect_manuals:
    manual = []
    for num in incorrect_manual:
        befores = rules.get(num, [])
        max_index = -1
        for before in befores:
            try:
                index = manual.index(before)
                max_index = max(index, max_index)
            except ValueError:
                pass
        manual.insert(max_index + 1, num)
    corrected_manuals.append(manual)

# 5. compute the answer
answer = sum(manual[len(manual) // 2] for manual in corrected_manuals)
print(answer)
