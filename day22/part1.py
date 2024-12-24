nums = []
with open("input.txt") as f:
    nums = [int(line.rstrip()) for line in f]

answer = 0
for secret in nums:
    for _ in range(2000):
        secret = (secret ^ (secret << 6)) & 16777215
        secret = (secret ^ (secret >> 5)) & 16777215
        secret = (secret ^ (secret << 11)) & 16777215
    answer += secret

print(answer)
