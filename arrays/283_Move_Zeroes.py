# ============================================================
#  Problem  : 283. Move Zeroes
#  Link     : https://leetcode.com/problems/move-zeroes/
#  Platform : LeetCode
#  Topic    : Array / Two Pointer
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. Use two pointers: left (tracks the position for the next non-zero element) and right (scans ahead).
#  2. When right finds a non-zero element, swap it with the element at left.
#  3. Increment left after each swap.
#  4. This moves all non-zero elements to the front while pushing zeroes to the back.
#
#  Example:
#  Input  : nums = [0,1,0,3,12]
#  Output : [1,3,12,0,0]
#
#  Time Complexity  : O(n) — single pass through the array
#  Space Complexity : O(1) — in-place, no extra space
# ============================================================

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes(nums)
    print(nums)  # [1,3,12,0,0]
