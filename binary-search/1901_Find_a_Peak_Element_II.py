# ============================================================
#  Problem  : 1901. Find a Peak Element II
#  Link     : https://leetcode.com/problems/find-a-peak-element-ii/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  Use binary search on columns. For a middle column, find the 
#  index of the maximum element. Check its horizontal neighbors. 
#  If it is greater than neighbors, it is a peak. Otherwise, 
#  move the search space toward the larger neighbor.
#
#  Example:
#  Input  : mat = [[1,4],[3,2]]
#  Output : [0,1] or [1,0]
#
#  Time Complexity  : O(n log m)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def maxeleincol(self, mat, col):
        n = len(mat)
        max_val = float('-inf')
        index = -1
        for i in range(n):
            if mat[i][col] > max_val:
                max_val = mat[i][col]
                index = i
        return index

    def findPeakGrid(self, mat):
        n = len(mat)
        m = len(mat[0])

        low = 0
        high = m - 1
        while low <= high:
            mid = (low+high)//2
            row = self.maxeleincol(mat, mid)
            left = mat[row][mid-1] if mid - 1 >=0 else float('-inf')
            right = mat[row][mid+1] if mid + 1 < m else float('-inf')

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row,mid]
            elif left > mat[row][mid]:
                high = mid - 1
            else:
                low = mid + 1
        return [-1,-1] 


# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakGrid([[1,4],[3,2]])) # Expected: [0,1] or [1,0]
