# Solution 1 - Brute Force
# Time : O(nm)
# Space : O(n+m)

class Solution1:
    def setZeroes(self, matrix: list[list[int]]) -> None:

        m, n = len(matrix), len(matrix[0])

        # Saving positions of 0
        rows = []
        cols = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        # Checking each index position and giving the element index to 0
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0


