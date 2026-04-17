# ============================================================
#  Problem  : Search a 2D Matrix
#  Link     : https://leetcode.com/problems/search-a-2d-matrix/
#  Platform : LeetCode
#  Topic    : Binary Search / Matrix
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  Treat the 2D matrix as a 1D sorted array by mapping the mid 
#  index to a 2D row/col coordinate (row = mid // cols, col = mid % cols).
#  Then, perform a standard binary search.
#
#  Time Complexity  : O(log(m * n))
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        low = 0
        high = n*m - 1
        while low <= high:
            mid = (low+high)//2
            row = mid//m
            col = mid%m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))  # True
