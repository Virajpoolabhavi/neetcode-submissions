class Solution:
    def isAlienSorted(self, nums: List[str], order: str) -> bool:
        rank = {}

        for i,ch in enumerate(order):
            rank[ch] = i
        

        for i in range(len(nums)-1):
            word1 = nums[i]
            word2 = nums[i+1]

            min_length = min(len(word1),len(word2))

            difference = False

            for j in range(min_length):

                if word1[j]!=word2[j]:
                    if rank[word1[j]] > rank[word2[j]]:
                        return False

                    difference = True
                    break
            
            if not difference and len(word1) > len(word2):
                return False
        return True

