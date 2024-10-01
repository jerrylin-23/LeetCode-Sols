class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+","*","-","/"}
        stack = []

        for char in tokens:
            val1 = 0
            val2 = 0
            if char not in operators:
                stack.append(int(char))
            else:
                if char == "+":
                    val1 = stack[-1]
                    stack.pop()
                    val2 = stack[-1]
                    stack.pop()
                    stack.append(val1 + val2)
                elif char == "-":
                    val1 = stack[-1]
                    stack.pop()
                    val2 = stack[-1]
                    stack.pop()
                    stack.append(val2 - val1)
                elif char == "/":
                    val1 = stack[-1]
                    stack.pop()
                    val2 = stack[-1]
                    stack.pop()
                    stack.append(int(val2 / val1))
                elif char == "*":
                    val1 = stack[-1]
                    stack.pop()
                    val2 = stack[-1]
                    stack.pop()
                    stack.append(val1 * val2)
                
        return stack[-1]

                    
