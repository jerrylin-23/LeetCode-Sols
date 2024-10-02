class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = defaultdict(int)
        max_count = 0
        max_len = 0
        left = 0

        for right in range(len(s)): 
            char_count[s[right]] += 1
            max_count = max(max_count, char_count[s[right]])
            #how would I be able to track what is being replaced
            if (right - left + 1) - max_count > k:
                char_count[s[left]] -=1
                left = left + 1
            
            max_len = max(max_len, right - left + 1)

        return max_len
            


