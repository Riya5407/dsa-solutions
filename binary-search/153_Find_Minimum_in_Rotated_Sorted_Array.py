# ============================================================
#  Problem  : 153. Find Minimum in Rotated Sorted Array
#  Link     : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. In a rotated sorted array, the minimum element is the only element that is smaller than its predecessor.
#  2. We use binary search to find this "pivot" point.
#  3. If nums[mid] > nums[high], it means the pivot is to the right of mid, so low = mid + 1.
#  4. Otherwise, the pivot is at mid or to the left, so high = mid.
#  5. Finally, low will point to the minimum element.
#
#  Example:
#  Input  : nums = [3,4,5,1,2]
#  Output : 1
#
#  Time Complexity  : O(log n) — halved search space at each step.
#  Space Complexity : O(1) — constant extra space.
# ============================================================

class Solution(object):
    def findMin(self, nums):
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))
