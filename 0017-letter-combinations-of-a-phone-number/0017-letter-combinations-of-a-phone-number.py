class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        result = []

        def backtrack (idx, substr): 
            if idx == len(digits):
                result.append(substr)
            mapped_str = map[digits[idx]]
            for char in mapped_str:
                backtrack (idx + 1 , substr + char)


        if digits:
            backtrack (0, "")
        return result