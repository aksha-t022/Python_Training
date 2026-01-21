class Solution:
    def removeDuplicates(self, nums):
        c = 0
        for i in range(1, len(nums)):
            if nums[c] != nums[i]:
                c += 1
                nums[c] = nums[i]
        return c + 1

# call the function
nums = [1, 1, 2]
s = Solution()
k = s.removeDuplicates(nums)

print("k =", k)
print("nums =", nums[:k])