class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0

        for char in s:
                if char.isdigit():
                    current_num = current_num * 10 + int (char)
                elif char == '[':
                    stack.append((current_string, current_num))
                    current_string = ""
                    current_num = 0
                elif char == ']':
                     prev_string, repeat_times = stack.pop()
                     current_string = prev_string + current_string * repeat_times
                else:
                    current_string += char
            
        return current_string
