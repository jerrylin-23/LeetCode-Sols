class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)

        furtherest = 0 

        for i in range(n):
            jump = nums[i]
            if i > furtherest:
                return False
            furtherest = max(furtherest, i + nums[i])
        return True
        