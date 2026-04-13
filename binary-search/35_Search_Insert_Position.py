# ============================================================
#  Problem  : 35. Search Insert Position
#  Link     : https://leetcode.com/problems/search-insert-position/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. We need to find the index where 'target' would be if it were inserted in order.
#  2. This is essentially finding the smallest index 'ans' such that nums[ans] >= target.
#  3. Use binary search (low and high pointers).
#  4. If nums[mid] >= target, mid is a potential answer, but there might be a smaller index to the left, so high = mid - 1.
#  5. If nums[mid] < target, the answer must be to the right, so low = mid + 1.
#
#  Example:
#  Input  : nums = [1,3,5,6], target = 5
#  Output : 2
#
#  Time Complexity  : O(log n) — standard binary search.
#  Space Complexity : O(1) — iterative approach using only pointers.
# ============================================================

class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchInsert([1, 3, 5, 6], 5))
