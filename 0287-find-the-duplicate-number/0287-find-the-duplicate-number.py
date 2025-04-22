class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        found = {}


        for num in nums:
            if num not in found:
                found[num] = 1
            else:
                return num