class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def CanEatAll(k):
            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k
            return hours <= h 

        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2 
            if (CanEatAll(mid)):
                high = mid -1
            else:
                low = mid + 1
        
        return low
