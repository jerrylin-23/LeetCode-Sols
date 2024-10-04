class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []


        def backtrack (remaining, combinations, start):
            if remaining == 0:
                result.append(list(combinations))
                return
            elif remaining < 0:
                return
            for i in range(start, len(candidates)):
                combinations.append(candidates[i])
                backtrack(remaining - candidates[i], combinations, i)
                combinations.pop()


        backtrack(target, [], 0)
        return result 