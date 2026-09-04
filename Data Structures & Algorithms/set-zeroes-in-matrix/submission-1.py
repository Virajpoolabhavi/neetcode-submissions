from collections import deque
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        zero_r = set()
        zero_c = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_r.add(i)
                    zero_c.add(j)
        
        for i in range(rows):
            for j in range(cols):
                if i in zero_r or j in zero_c:
                    matrix[i][j] = 0
        







        
        
        