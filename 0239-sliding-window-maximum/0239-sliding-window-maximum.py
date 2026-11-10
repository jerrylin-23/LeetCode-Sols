import heapq

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = []
        result = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            # Remove expired entries from the top.
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            if i >= k - 1:
                result.append(-heap[0][0])

        return result