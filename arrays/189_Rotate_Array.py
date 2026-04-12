# ============================================================
#  Problem  : 189. Rotate Array
#  Link     : https://leetcode.com/problems/rotate-array/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Handle cases where k is greater than the array length by taking k % n.
#  2. Use Python's slicing feature to rotate the array in-place.
#  3. `nums[-k:]` gives the last k elements, and `nums[:-k]` gives the rest.
#  4. Combine them and assign back to `nums[:]` to modify the original reference.
#
#  Example:
#  Input  : nums = [1,2,3,4,5,6,7], k = 3
#  Output : [5,6,7,1,2,3,4]
#
#  Time Complexity  : O(n) — slicing and concatenation both take linear time.
#  Space Complexity : O(n) — slicing creates new list fragments.
# ============================================================

class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    test_nums = [1,2,3,4,5,6,7]
    sol.rotate(test_nums, 3)
    print(test_nums)
