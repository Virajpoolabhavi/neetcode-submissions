class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergeSort(nums):
            if len(nums)<=1:
                return nums
            
            mid = len(nums)//2

            left_half = mergeSort(nums[:mid])
            right_half = mergeSort(nums[mid:])

            return merge(left_half,right_half,nums)

        def merge(left,right,nums):
            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i+=1
                    k+=1
                else:
                    nums[k] =  right[j]
                    j+=1
                    k+=1

            while i < len(left):
                nums[k] = left[i]
                i+=1
                k+=1
            while j < len(right):
                nums[k] = right[j]
                j+=1
                k+=1
            return nums
        return mergeSort(nums)
