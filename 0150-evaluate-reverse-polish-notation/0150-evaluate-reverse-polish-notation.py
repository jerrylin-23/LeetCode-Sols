class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "/", "*" }

        for char in tokens:
            if char in operators:
                a = stack.pop()
                b = stack.pop()
                if char == "+":
                    stack.append(a + b)
                if char == "-":
                    stack.append(b - a)
                if char == "/":
                    stack.append(int(b / a))
                if char == "*":
                    stack.append(a * b)
            else:
                stack.append(int(char))
        
        return stack[0]