class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n =  len(nums) 
        dp_max = [0] * n
        dp_min = [0] * n

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        result = nums[0]


        for i in range (1, n):
            dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            result = max(result, dp_max[i])
        
        return result