class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_freq = {0:1}
        current_prefix = 0
        result = 0

        for num in nums:
            current_prefix += num

            needed_prefix = current_prefix - k

            if needed_prefix in pre_freq:
                result += pre_freq[needed_prefix]

            pre_freq[current_prefix] = pre_freq.get(current_prefix,0)+1
        return result 
 


        