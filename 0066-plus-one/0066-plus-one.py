class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        
        digits[length - 1] += 1

        for i in range (length - 1, -1 , -1):
            if digits[i] == 10:
                digits [i] = 0
                if i > 0:
                    digits[i - 1] += 1
                else:
                    digits.insert(0,1)
        
        return digits


        return List