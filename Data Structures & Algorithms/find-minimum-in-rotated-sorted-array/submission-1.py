class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float('inf')

        for n in nums:
            if n < minimum:
                minimum = n
        return minimum

        