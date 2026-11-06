class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        low, high = 0, max(diffs)

        while low < high:
            limit = (low + high) // 2

            needed = sum(max(0, d - limit) for d in diffs)

            if needed > k:
                low = limit + 1
            else:
                high = limit

        limit = low

        # Reduce every difference to at most the limit.
        for i in range(len(diffs)):
            if diffs[i] > limit:
                k -= diffs[i] - limit
                diffs[i] = limit

        # Use the remaining operations on differences at the limit.
        for i in range(len(diffs)):
            if k == 0:
                break

            if diffs[i] == limit:
                diffs[i] -= 1
                k -= 1

        return sum(d * d for d in diffs)