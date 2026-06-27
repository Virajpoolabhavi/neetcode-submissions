class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            if i not in ans:
                if nums.count(i) > len(nums)//3:
                    ans.append(i)
        
        return ans
        