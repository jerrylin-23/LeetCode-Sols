class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: s1 is longer than s2
        if len(s1) > len(s2):
            return False
            
        s1_dict = {}
        s2_dict = {}
        window = len(s1)
        
        # Build character frequency dictionary for s1
        for char in s1:
            if char not in s1_dict:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1
        
        # Initialize the first window
        for i in range(window):
            char = s2[i]
            if char not in s2_dict:
                s2_dict[char] = 1
            else:
                s2_dict[char] += 1
        
        # Check if first window matches
        if s1_dict == s2_dict:
            return True
            
        # Slide the window
        for right in range(window, len(s2)):
            # Add the new character
            if s2[right] not in s2_dict:
                s2_dict[s2[right]] = 1
            else:
                s2_dict[s2[right]] += 1
                
            # Remove the leftmost character
            left = right - window
            s2_dict[s2[left]] -= 1
            if s2_dict[s2[left]] == 0:
                del s2_dict[s2[left]]
                
            # Check if current window is a permutation
            if s1_dict == s2_dict:
                return True
                
        return False