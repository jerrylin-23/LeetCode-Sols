class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for y in range (i + 1, n, 1):
                if nums[i] + nums[y] == target:
                    return i, y
