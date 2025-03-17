class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_collection = defaultdict(list)

        for s in strs: 
            s_sorted = "".join(sorted(s))
            anagrams_collection[s_sorted].append(s)
        return list(anagrams_collection.values())