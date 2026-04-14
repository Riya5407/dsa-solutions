# ============================================================
#  Problem  : 1482. Minimum Number of Days to Make m Bouquets
#  Link     : https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. This is a "Binary Search on Answer" problem.
#  2. The possible range of days is [min(bloomDay), max(bloomDay)].
#  3. For a chosen day X, check if we can pick m bouquets of k adjacent flowers.
#  4. If yes, try fewer days (high = mid - 1).
#  5. If no, try more days (low = mid + 1).
#
#  Example:
#  Input  : bloomDay = [1,10,3,10,2], m = 3, k = 1
#  Output : 3
#
#  Time Complexity  : O(n * log(max_day - min_day))
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def is_possible(self, bloomDay, days, m, k):
        count = 0
        bouq = 0
        for bloom in bloomDay:
            if bloom <= days:
                count += 1
                if count == k:
                    bouq += 1
                    count = 0
            else:
                count = 0
        return bouq >= m

    def minDays(self, bloomDay, m, k):
        # Impossible if we don't have enough flowers total
        if m * k > len(bloomDay):
            return -1
        
        low = min(bloomDay)
        high = max(bloomDay)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if self.is_possible(bloomDay, mid, m, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.minDays([1, 10, 3, 10, 2], 3, 1))  # Expected: 3
    print(sol.minDays([1, 10, 3, 10, 2], 3, 2))  # Expected: -1
