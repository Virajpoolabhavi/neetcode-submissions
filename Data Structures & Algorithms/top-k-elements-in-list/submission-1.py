class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = d.get(num, 0) + 1

        freq_sorted = sorted(d.items(), key=lambda x: x[1], reverse=True)

        return [key for key, value in freq_sorted[:k]]
        