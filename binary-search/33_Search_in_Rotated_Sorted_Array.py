# ============================================================
#  Problem  : 33. Search in Rotated Sorted Array
#  Link     : https://leetcode.com/problems/search-in-rotated-sorted-array/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Use binary search with a slight modification for rotation.
#  2. Calculate mid. If nums[mid] is target, return mid.
#  3. Determine which side is sorted (low to mid OR mid to high).
#  4. If left side is sorted: check if target is in [low, mid].
#  5. If right side is sorted: check if target is in [mid, high].
#  6. Narrow search space based on the above.
#
#  Example:
#  Input  : nums = [4,5,6,7,0,1,2], target = 0
#  Output : 4
#
#  Time Complexity  : O(log n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            
            # Identify the sorted half
            if nums[low] <= nums[mid]:
                # Left half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 0))  # Expected: 4
    print(sol.search([4, 5, 6, 7, 0, 1, 2], 3))  # Expected: -1
