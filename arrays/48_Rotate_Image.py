# ============================================================
#  Problem  : 48. Rotate Image
#  Link     : https://leetcode.com/problems/rotate-image/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. First, transpose the matrix: swap elements `matrix[i][j]` with `matrix[j][i]` for all valid `i` and `j` where `j > i`.
#  2. After transposing, reverse each row of the matrix.
#  3. And boom, the matrix is now rotated 90 degrees clockwise in-place!
#
#  Example:
#  Input  : [[1,2,3],[4,5,6],[7,8,9]]
#  Output : [[7,4,1],[8,5,2],[9,6,3]]
#
#  Time Complexity  : O(N^2) — we iterate through all N^2 elements of the matrix twice (once for transpose, once for reversing rows).
#  Space Complexity : O(1) — all operations are performed in-place, modifying the original matrix directly.
# ============================================================

class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(i+1,m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()
    

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
