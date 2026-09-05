from collections import deque
from string import ascii_lowercase
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord,1))

        while queue:
            word , level = queue.popleft()

            if word == endWord:
                return level

            for i in range(len(word)):
                for char in ascii_lowercase:
                    newWord = word[:i] + char + word[i+1: ]

                    if newWord in wordSet:
                        wordSet.remove(newWord)

                        queue.append((newWord,level+1))
        return 0

        