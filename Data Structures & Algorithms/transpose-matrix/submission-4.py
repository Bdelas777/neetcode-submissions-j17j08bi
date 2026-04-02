class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r,c = len(matrix), len(matrix[0])
        res = [[0]* r for i in range(c)]
        for row in range(r):
            for col in range(c):
                res[col][ row] = matrix[row][col]
        return res



