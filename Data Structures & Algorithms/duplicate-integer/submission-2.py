class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return True
        #     else :
        #         seen.add(num)
        # return False

        seen = set(nums)

        return True if len(nums) != len(seen) else False