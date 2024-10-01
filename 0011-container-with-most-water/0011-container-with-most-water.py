class Solution:
    def maxArea(self, height: List[int]) -> int:
        n  = len (height)
        left = 0 
        right = n - 1
        max_area = 0 

        while left < right:
            
            area = min(height[left], height[right]) *  (right - left) 
            max_area = max (area, max_area)

            if height[left] < height[right]: 
                left = left + 1
            else: 
                right = right -1
        
        
        return max_area