class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        wordset = set(words)
        memo = {}

        def dfs(word):
            if word in memo:
                return memo[word]

            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in wordset and (suffix in wordset or dfs(suffix)):
                    memo[word] = True
                    return True

            memo[word] = False
            return False

        result = []
        for word in wordset:
            if dfs(word):
                result.append(word)

        return result