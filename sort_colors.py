class Solution:
    def sortColors(self, nums):
        count0 = count1 = count2 = 0

        for v in nums:
            if v == 0:
                count0 += 1
            elif v == 1:
                count1 += 1
            else:
                count2 += 1

        ind = 0

        while ind < count0:
            nums[ind] = 0
            ind += 1

        while ind < count0 + count1:
            nums[ind] = 1
            ind += 1

        while ind < count0 + count1 + count2:
            nums[ind] = 2
            ind += 1
        return nums