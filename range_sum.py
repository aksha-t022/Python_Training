class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)

    def sumRange(self, left, right):
        return self.prefix[right + 1] - self.prefix[left]


nums = list(map(int, input("Enter numbers: ").split()))
obj = NumArray(nums)

q = int(input("Enter number of queries: "))
for _ in range(q):
    l, r = map(int, input().split())
    print(obj.sumRange(l, r))
