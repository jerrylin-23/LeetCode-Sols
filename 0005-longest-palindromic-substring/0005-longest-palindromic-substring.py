class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 1:
            return ""

        start = end = 0 

        for i in range (len(s)):
            odd = self.expandAroundCenter(s, i, i)
            even = self.expandAroundCenter(s, i, i + 1)
            max_len = max(even, odd)

            if max_len > (end - start):
                start = i - (max_len - 1) // 2
                end = i + (max_len) // 2 

        return  s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[right]==s[left]:
            right +=1 
            left -=1
        return right - left - 1 






