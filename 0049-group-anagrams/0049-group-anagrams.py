class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            s_sorted = "".join(sorted(s))
            anagrams_dict[s_sorted].append(s)
    

        return list(anagrams_dict.values())