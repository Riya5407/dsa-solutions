# ============================================================
#  Problem  : 73. Set Matrix Zeroes
#  Link     : https://leetcode.com/problems/set-matrix-zeroes/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. First, use the first row and first column as markers to record if a row or column needs to be zeroed out.
#  2. Handle the special case of `matrix[0][0]` which acts as a marker for both the first row and first column, by using a separate variable (`col0`) to track if the first column needs to be zeroed.
#  3. Then, iterate through the matrix (starting from `(1,1)`) and set elements to zero if their corresponding marker in the first row or first column indicates they should be zeroed.
#  4. Finally, process the first row and first column based on their markers and the `col0` variable to set them to zero if necessary.
#
#  Example:
#  Input  : [[1,1,1],[1,0,1],[1,1,1]]
#  Output : [[1,0,1],[0,0,0],[1,0,1]]
#
#  Time Complexity  : O(M*N) — We iterate through the M x N matrix a constant number of times.
#  Space Complexity : O(1) — We use only a few extra variables, not dependent on the input size.
# ============================================================

class Solution(object):
    def setZeroes(self, matrix):
        col0 = 1
        n = len(matrix)
        m = len(matrix[0])
        for i in range(0,n):
            for j in range(0,m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0

        for i in range(1,n):
            for j in range(1,m):
                if matrix[i][j] != 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:
                        matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0
        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

        return matrix

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
