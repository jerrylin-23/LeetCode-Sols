class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}
        for i in range(len(s)):
            if s[i] not in my_dict: 
                my_dict[s[i]] = i
            else:
                my_dict[s[i]] = -1
        

        for key, value in my_dict.items():
            if value != -1:
                return value
        
        return -1