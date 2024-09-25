class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False


        char_to_word = {}
        word_to_char = {}
        

        for c, word in zip (pattern, words):
            if c in char_to_word:
                if char_to_word[c] != word: 
                    return False
            else: 
                char_to_word[c] = word
            if word in word_to_char:
                if word_to_char[word] != c:
                    return False
            else: 
                word_to_char[word] = c

        return True