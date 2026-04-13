# ============================================================
#  Problem  : 704. Binary Search
#  Link     : https://leetcode.com/problems/binary-search/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. Initialize two pointers: low at 0 and high at n-1.
#  2. Use a recursive (or iterative) helper to find the target.
#  3. Calculate mid as (low + high) // 2.
#  4. If nums[mid] is the target, return mid.
#  5. If target is smaller than nums[mid], search in the left half.
#  6. If target is larger than nums[mid], search in the right half.
#  7. If low exceeds high, the target is not in the array (-1).
#
#  Example:
#  Input  : nums = [-1,0,3,5,9,12], target = 9
#  Output : 4
#
#  Time Complexity  : O(log n) — because we're halving the search space at each step.
#  Space Complexity : O(log n) — due to the recursive call stack (O(1) if iterative).
# ============================================================

class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        
        def binary(nums, low, high, target):
            if low > high:
                return -1
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary(nums, low, mid-1, target)
            else:
                return binary(nums, mid+1, high, target)
        return binary(nums, low, high, target)

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.search([-1, 0, 3, 5, 9, 12], 9))
