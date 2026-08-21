class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}

        for word in strs:
            count = [0] *26

            for c in word:
                count[ord(c) - ord('a')] +=1

            key = tuple(count)

            if key not in grp:
                grp[key] = []

            grp[key].append(word)
        return list(grp.values())

        
        