class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        word_window = []
        for char in s:
            if char == " ":
                if word_window:
                    result.append("".join(word_window))
                    word_window = []
                continue
            word_window.append(char)
        if word_window:
            result.append("".join(word_window))
        
        result = result[::-1]

        return " ".join(result)
