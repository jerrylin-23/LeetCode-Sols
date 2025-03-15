class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):
            for k in range(i + 1, n):
                if nums[i] + nums[k] == target:
                    return [i, k]