# ============================================================
#  Problem  : 540. Single Element in a Sorted Array
#  Link     : https://leetcode.com/problems/single-element-in-a-sorted-array/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. In a sorted array where every element appears twice except one,
#     pairs start at even indices (0, 2, 4...).
#  2. If the single element is to the right, a pair starting at mid (even) 
#     will have nums[mid] == nums[mid+1].
#  3. If we find this property is broken, the single element is to the left.
#  4. Check parity of mid to decide which half to discard.
#
#  Example:
#  Input  : nums = [1,1,2,3,3,4,4,8,8]
#  Output : 2
#
#  Time Complexity  : O(log n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def singleNonDuplicate(self, nums):
        n = len(nums)
        # Edge cases
        if n == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[n-1] != nums[n-2]: return nums[n-1]
        
        low, high = 1, n - 2
        while low <= high:
            mid = (low + high) // 2
            
            # Found the single element
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            
            # Check pair property (even-odd or odd-even)
            # If we are on the left side of the single element:
            # - mid is odd and nums[mid] == nums[mid-1]
            # - mid is even and nums[mid] == nums[mid+1]
            if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
                low = mid + 1
            else:
                high = mid - 1
        return -1

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))  # Expected: 2
    print(sol.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))     # Expected: 10
