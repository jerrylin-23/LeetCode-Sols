class Solution:
    def minOperations(self, nums: List[int]) -> int:
        zero_pos = nums.index(0)

        backwards = True
        forwards = True

        n = len(nums)

        for i in range(n):
            if nums[(zero_pos + i) % n] != i:
                forwards = False 
            if nums[(zero_pos - i) % n] != i:
                backwards = False 

        if forwards:
            return min(zero_pos, n - zero_pos + 2)
        if backwards:
            return min(zero_pos + 2, n - zero_pos)
        
        return -1


        
        