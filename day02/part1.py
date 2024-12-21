count = 0
with open("input.txt") as f:
    for line in f:
        line = line.rstrip()
        nums = [int(num) for num in line.split()]
        decreasing = nums[1] < nums[0]
        safe = True
        for i in range(1, len(nums)):
            cur = nums[i]
            prev = nums[i - 1]
            if not (1 <= abs(cur - prev) <= 3):
                safe = False
                break
            if (decreasing and cur > prev) or (not decreasing and cur < prev ):
                safe = False
                break
        if safe:
            count += 1

print(count)
