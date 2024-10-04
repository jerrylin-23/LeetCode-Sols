class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def backtrack(subset):
            if len(subset) == n:
                result.append(list(subset))
                return
            for i in range (len(nums)):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    backtrack(subset)
                    subset.pop()



        backtrack ([])
        return result
                

