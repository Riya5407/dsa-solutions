# ============================================================
#  Problem  : 81. Search in Rotated Sorted Array II
#  Link     : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Similar to Search in Rotated Sorted Array I, but handles duplicates.
#  2. If nums[low], nums[mid], and nums[high] are all equal, we can't tell 
#     which side is sorted. Narrow the search space by low += 1 and high -= 1.
#  3. Otherwise, proceed with determining the sorted half.
#
#  Example:
#  Input  : nums = [2,5,6,0,0,1,2], target = 0
#  Output : True
#
#  Time Complexity  : O(log n) on average, O(n) in worst case (all duplicates).
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            
            # Handle duplicates edge case
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
                
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
        return False

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([2, 5, 6, 0, 0, 1, 2], 0))  # Expected: True
    print(sol.search([2, 5, 6, 0, 0, 1, 2], 3))  # Expected: False
