# ============================================================
#  Problem  : 88. Merge Sorted Array
#  Link     : https://leetcode.com/problems/merge-sorted-array/
#  Platform : LeetCode
#  Topic    : Array / Two Pointer
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. Use three pointers: i at end of nums1's elements, j at end of nums2, k at end of merged array.
#  2. Compare nums1[i] and nums2[j] from the back and place the larger one at position k.
#  3. If nums2 still has remaining elements after nums1 is exhausted, fill them in.
#  4. This avoids overwriting nums1 elements before they're processed.
#
#  Example:
#  Input  : nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#  Output : [1,2,2,3,5,6]
#
#  Time Complexity  : O(m + n) — single pass through both arrays
#  Space Complexity : O(1) — in-place, no extra space
# ============================================================

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,0,0,0]
    sol.merge(nums1, 3, [2,5,6], 3)
    print(nums1)  # [1,2,2,3,5,6]
