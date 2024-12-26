class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr_set = set()
        for num in nums:
            if num not in arr_set:
                arr_set.add(num)
            else:
                return True
        
        return False


        