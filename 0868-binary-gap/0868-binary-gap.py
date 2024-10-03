class Solution:
    def binaryGap(self, n: int) -> int:
        binary = ""
        while n > 0:
            binary_num = n % 2
            binary = str(binary_num) + binary
            n //= 2

        max_len = 0
        counter = 0
        first_one = False
        for char in binary:
            if char == '1':
                if first_one: 
                    max_len = max(max_len , counter) 
                first_one = True
                counter = 1
            elif char == '0' and first_one:
                counter += 1
        return max_len