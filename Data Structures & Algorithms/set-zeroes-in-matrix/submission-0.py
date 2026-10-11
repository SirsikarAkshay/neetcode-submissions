class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])

        hasht = {"rows":set(), "cols":set()}

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    hasht["rows"].add(i)
                    hasht["cols"].add(j)
            
        for i in range(n):
            for j in range(m):
                if i in hasht["rows"] or j in hasht["cols"]:
                    matrix[i][j] = 0
                