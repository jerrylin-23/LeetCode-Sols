class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat (spd, list, time):
            counter = 0
            for num in piles:
                counter += math.ceil(num / spd)
                if counter > time:
                    return False
            return True

        left , right = 1 , max(piles)

        while left <= right: 
            mid = (left + right) // 2
            
            if canEat(mid, piles, h):
                right = mid - 1 
            else:
                left = mid + 1

        return left
                    


            