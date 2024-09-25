class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
                if b == 0:
                    return a 
                else:
                    return gcd(b, a % b)
    
        gcd_length  = gcd(len(str1), len(str2))


        gcd_string = str1[:gcd_length]

        for i in range (0, len(str1), gcd_length):
            if str1[i: i + gcd_length] != gcd_string:
                return ""
        


        for i in range (0, len(str2), gcd_length):
            if str2[i:i + gcd_length] != gcd_string:
                return ""
        

        return gcd_string

        