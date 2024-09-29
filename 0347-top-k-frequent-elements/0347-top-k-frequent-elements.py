class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        elements = {}
 
        for i in nums:
            if i in elements:
                elements[i] += 1
            else: 
                elements[i] = 1
        
        top_k_largest = sorted(elements.items(), key=lambda x: x[1], reverse=True)[:k]

        return [item[0] for item in top_k_largest]
