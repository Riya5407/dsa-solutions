# ============================================================
#  Problem  : Sort Colors
#  Link     : https://leetcode.com/problems/sort-colors/
#  Platform : LeetCode
#  Topic    : Two Pointer (Dutch National Flag)
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  Use the Dutch National Flag algorithm with three pointers: 
#  low, mid, and high. Array elements are grouped dynamically
#  by swapping 0s to the front, 2s to the end, and skipping 1s.
#
#  Time Complexity  : O(n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    arr = [2,0,2,1,1,0]
    sol.sortColors(arr)
    print("Test 1:", arr)
