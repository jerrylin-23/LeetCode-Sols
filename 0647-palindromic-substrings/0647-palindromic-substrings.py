class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        counter = 0

        def expandcenter (left, right):
            count = 0
            while left >= 0 and right < n and s[right] == s[left]:
                right += 1
                left -= 1
                count += 1
            return count
        

        for i in range(n):
            odd = expandcenter (i, i)
            even = expandcenter (i,i+1)
            counter += (odd + even)
        return counter