class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        word_set = set(words)
        result = []

        for target in words:
            if not target:
                continue

            memo = {}

            def dfs(start):
                if start == len(target):
                    return True

                if start in memo:
                    return memo[start]

                for end in range(start + 1, len(target) + 1):
                    # Prevent using the entire target as one piece.
                    if start == 0 and end == len(target):
                        continue

                    piece = target[start:end]

                    if piece in word_set:
                        if dfs(end):
                            memo[start] = True
                            return True

                memo[start] = False
                return False

            if dfs(0):
                result.append(target)

        return result