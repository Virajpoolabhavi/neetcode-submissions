class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement]+1,i+1]

            else:
                seen[nums[i]] = i
        return 0
        