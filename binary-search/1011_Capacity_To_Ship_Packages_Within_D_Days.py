# ============================================================
#  Problem  : Capacity To Ship Packages Within D Days
#  Link     : https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  We can use binary search on the answer. The minimum possible capacity is
#  the maximum weight in the array (since we can't split a package), and the
#  maximum is the sum of all weights. For a given capacity, we check how many
#  days are needed and adjust our binary search range accordingly.
#
#  Time Complexity  : O(N * log(Sum - Max))
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def daysneeded(self, weights, capacity):
        days = 1
        currentload = 0
        for w in weights:
            if currentload + w > capacity:
                days += 1
                currentload = w
            else:
                currentload += w
        return days

    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low+high)//2
            needed = self.daysneeded(weights,mid)
            if needed <= days:
                high = mid
            else:
                low = mid + 1
        return low

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    solution = Solution()
    print(solution.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5)) # Expected: 15
