class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range(1,len(nums)):
            x = nums[i]

            prev_max = curr_max
            prev_min = curr_min

            curr_max = max(x,prev_max*x, prev_min*x)
            curr_min = min(x,prev_max*x, prev_min*x)

            result = max(result, curr_max)
        return result 
        