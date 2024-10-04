class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def palindrome (substr):
            return substr == substr[::-1]


        def backtrack (start, substr):
            if start == len(s):
                result.append(substr.copy())
                return
            for i in range (start, len(s)):
                if palindrome (s[start: i + 1 ]):
                    substr.append(s[start:i + 1])
                    backtrack(i + 1, substr)
                    substr.pop()

        backtrack(0, [])


        return result
