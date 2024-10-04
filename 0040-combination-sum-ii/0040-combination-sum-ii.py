class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        candidates.sort()
        def backtrack(difference, start, subset):
            if difference == 0:
                result.append(list(subset))
            if difference < 0:
                return
            

            for i in range (start, len(candidates)):
                if i > start and candidates[i] == candidates[ i - 1]:
                    continue
                subset.append(candidates[i])
                backtrack(difference - candidates[i], i + 1,  subset)
                subset.pop()
        
        backtrack(target, 0, [])

        return result