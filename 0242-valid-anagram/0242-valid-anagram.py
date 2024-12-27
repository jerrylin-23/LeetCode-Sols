class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for char in s: 
            if char not in my_dict:
                my_dict[char] = 1
            else:
                my_dict[char] += 1
        

        for char in t:
            if char not in my_dict:
                my_dict[char] = -1
            else:
                my_dict[char] -= 1
        
        for key, value in my_dict.items():
            if value != 0:
                return False
        

        return True