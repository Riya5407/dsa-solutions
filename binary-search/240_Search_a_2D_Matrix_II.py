# ============================================================
#  Problem  : Search a 2D Matrix II
#  Link     : https://leetcode.com/problems/search-a-2d-matrix-ii/
#  Platform : LeetCode
#  Topic    : Binary Search / Matrix
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  Start from the top-right corner of the matrix. If the current element
#  is greater than the target, move left (col -= 1). If the current element
#  is less than the target, move down (row += 1). Repeat until found or out of bounds.
#
#  Time Complexity  : O(n + m)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        row = 0
        col = m-1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    print(solution.searchMatrix(matrix, 5))  # True
