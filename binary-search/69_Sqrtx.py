# ============================================================
#  Problem  : 69. Sqrt(x)
#  Link     : https://leetcode.com/problems/sqrtx/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. Handle the edge case of x = 0 immediately.
#  2. The search space for the square root is [1, x].
#  3. Use binary search to find the largest integer 'ans' such that ans * ans <= x.
#  4. If mid * mid <= x, mid is a valid candidate, so update ans = mid and search in the higher half (left = mid + 1).
#  5. Otherwise, search in the lower half (right = mid - 1).
#
#  Example:
#  Input  : x = 8
#  Output : 2 (since sqrt(8) = 2.828... and we return the integer part)
#
#  Time Complexity  : O(log x) — binary search on the range 1 to x.
#  Space Complexity : O(1) — no extra storage used.
# ============================================================

class Solution:
    def mySqrt(self, x):
        if x == 0:
            return 0
        left, right = 1, x
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(8))
