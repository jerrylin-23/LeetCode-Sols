class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)

        for i in range(len(s1)):
            s1_dict[s1[i]] += 1
        

        left = 0
        
        for right in range(len(s2)):
            s2_dict[s2[right]] += 1


            if right - left + 1 > len(s1):
                s2_dict[s2[left]] -= 1
                if s2_dict[s2[left]] == 0:
                    del s2_dict[s2[left]]
                left = left + 1



            if s1_dict == s2_dict:
                return True

        return False