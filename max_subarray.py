nums = list(map(int, input().split()))

cs = nums[0]
ms = nums[0]
for i in range(1, len(nums)):
    cs = max(nums[i], cs + nums[i])
    ms = max(ms, cs)

print(ms)
