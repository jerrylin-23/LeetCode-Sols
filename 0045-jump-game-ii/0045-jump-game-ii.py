class Solution:
    def jump(self, nums: list[int]) -> int:
        furtherest = 0 
        current_end = 0
        jumps = 0

        for i in range(len(nums) - 1):
            furtherest = max(furtherest , i + nums[i])

            if i == current_end:
                current_end = furtherest
                jumps += 1
            
        return jumps 

        