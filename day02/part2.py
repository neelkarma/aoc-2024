count = 0

def check_safe(nums):
    safe = True
    increasing = nums[1] > nums[0]
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if increasing and diff < 0:
            safe = False
            break
        if not increasing and diff > 0:
            safe = False
            break
        if not (1 <= abs(diff) <= 3):
            safe = False
            break
    return safe



with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        nums = [int(num) for num in line.split()]

        if check_safe(nums):
            count += 1
            continue

        # fuck it, we ball
        safe = False
        for removed_i in range(len(nums)):
            modified_nums = nums[:removed_i] + nums[removed_i + 1:]
            if check_safe(modified_nums):
                safe = True
                break
        if safe:
            count += 1

print(count)
