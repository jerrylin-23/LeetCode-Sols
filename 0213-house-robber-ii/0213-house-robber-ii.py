class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_help (nums):
            n = len(nums)
            dp = [0] * n

            if n == 1:
                return nums[0]
            
            dp[0] = nums[0]
            dp[1] = max(nums[1] , nums[0])

            for i in range(2 , n):
                dp[i] = max (dp[i - 1], dp[i-2] + nums[i])

            return dp[n - 1]
        n = len(nums)
        if n == 1:
            return nums[0]
        return max (rob_help(nums[:-1]), rob_help(nums[1:]))