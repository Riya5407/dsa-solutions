# ============================================================
#  Problem  : 118. Pascal's Triangle
#  Link     : https://leetcode.com/problems/pascals-triangle/
#  Platform : LeetCode
#  Topic    : Array / Dynamic Programming
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. The first row is always [1].
#  2. For each subsequent row, start and end with 1.
#  3. Each inner element is the sum of the two elements directly above it (from the previous row).
#  4. Append each completed row to the triangle list.
#
#  Example:
#  Input  : numRows = 5
#  Output : [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#  Time Complexity  : O(n^2) — we fill every cell of the triangle
#  Space Complexity : O(n^2) — storing the entire triangle
# ============================================================

class Solution(object):
    def generate(self, numRows):
        triangle = []
        for i in range(numRows):
            if i == 0:
                triangle.append([1])
            else:
                row = [1]
                prev = triangle[-1]
                for j in range(len(prev)-1):
                    row.append(prev[j] + prev[j+1])
                row.append(1)
                triangle.append(row)
        return triangle

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.generate(5))  # [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
