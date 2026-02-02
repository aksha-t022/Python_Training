nums = list(map(int, input().split()))

c = 0
m = None
for n in nums:
    if c == 0:
        m = n
    c += 1 if n == m else -1

print(m)
