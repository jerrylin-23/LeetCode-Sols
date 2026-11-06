class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        sorted_strs = sorted(strs, key = lambda x: len(x))

        n = len(sorted_strs[0])
        result = []

        for i in range(n):
            char = sorted_strs[0][i]
            for words in sorted_strs:
                if words[i] != char:
                    return "".join(result)
            result.append(char)
        
        return "".join(result)
        