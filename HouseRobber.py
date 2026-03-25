class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}

        def helpfunction(nums,index,size):
            if index>=size:
                return 0
            if index in dp:
                return dp[index]
            dp[index]=max(
                helpfunction(nums,index+1,size),
                nums[index]+helpfunction(nums,index+2,size),
            )
            return dp[index]
        return helpfunction(nums,0,len(nums))