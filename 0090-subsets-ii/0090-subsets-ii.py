class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        def backtrack (start, subset):
            result.append(list(subset))

            for i in range (start, n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack (i + 1, subset)
                subset.pop()

            
        backtrack(0, [])
        return result