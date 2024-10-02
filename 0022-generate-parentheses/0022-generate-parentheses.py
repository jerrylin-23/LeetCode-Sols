class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [("", 0, 0)]

        while stack:
            current_string, open_count, close_count = stack.pop()

            if len(current_string) == 2 * n:
                result.append(current_string)
                continue
            
            if open_count < n:
                stack.append((current_string + "(", open_count + 1, close_count))

        
            if close_count < open_count:
                stack.append((current_string + ")", open_count, close_count + 1))

        return result   