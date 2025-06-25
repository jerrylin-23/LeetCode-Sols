class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ')':'(',
                    '}':'{',
                    ']':'['
        }

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                else:
                    stack.pop()

        if not stack:
            return True
        else:
            return False