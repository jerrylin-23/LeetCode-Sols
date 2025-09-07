class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            sorted_str = tuple(sorted(s))
            if sorted_str in result:
                result[sorted_str].append(s)
            else:
                result[sorted_str] = [s]

        return list(result.values())