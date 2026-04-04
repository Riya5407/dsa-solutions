# ============================================================
#  Problem  : 54. Spiral Matrix
#  Link     : https://leetcode.com/problems/spiral-matrix/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Initialize four pointers: `top`, `bottom`, `left`, and `right` to define the boundaries of the matrix.
#  2. Loop as long as `top <= bottom` and `left <= right`, processing one layer of the spiral at a time.
#  3. First, traverse the `top` row from `left` to `right`, then increment `top`. Next, traverse the `right` column from `top` to `bottom`, then decrement `right`.
#  4. If rows and columns still exist, traverse the `bottom` row from `right` to `left`, then decrement `bottom`. Finally, traverse the `left` column from `bottom` to `top`, then increment `left`.
#
#  Example:
#  Input  : [[1,2,3],[4,5,6],[7,8,9]]
#  Output : [1,2,3,6,9,8,7,4,5]
#
#  Time Complexity  : O(m*n) — We visit each element in the m x n matrix exactly once.
#  Space Complexity : O(m*n) — We store all m*n elements in the result list.
# ============================================================

class Solution(object):
    def spiralOrder(self, matrix):
        result = []
        top = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        left = 0

        while top <= bottom and left <= right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1
        
            if left <= right:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left += 1

        return result

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
