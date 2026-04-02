class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r,c = len(matrix), len(matrix[0])
        res = [[0] * r for i in range(c)]
        for rows in range(r):
            for cols in range(c):
                res[cols][rows] = matrix[rows][cols]
        return res