# ============================================================
#  Problem  : 162. Find Peak Element
#  Link     : https://leetcode.com/problems/find-peak-element/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. A peak element is greater than its neighbors.
#  2. Use binary search: if nums[mid] > nums[mid+1], the peak must be 
#     at mid or to its left (since we've already found a "downslope").
#  3. Otherwise, search the right side.
#  4. The loop terminates when low and high meet at a peak.
#
#  Example:
#  Input  : nums = [1,2,3,1]
#  Output : 2 (index of 3)
#
#  Time Complexity  : O(log n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def findPeakElement(self, nums):
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[mid + 1]:
                # Decreasing side, peak is on the left (including mid)
                high = mid
            else:
                # Increasing side, peak is on the right
                low = mid + 1
        return low

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.findPeakElement([1, 2, 3, 1]))  # Expected: 2 (index of value 3)
    print(sol.findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # Expected: 1 or 5
