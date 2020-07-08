class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    continue
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True