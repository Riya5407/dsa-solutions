# ============================================================
#  Problem  : 34. Find First and Last Position of Element in Sorted Array
#  Link     : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Use binary search to find any one occurrence of the target.
#  2. Once found, use two pointers (start and end) to expand from that position to find the first and last occurrences.
#  3. If no occurrence is found, return [-1, -1].
#
#  Example:
#  Input  : nums = [5,7,7,8,8,10], target = 8
#  Output : [3,4]
#
#  Time Complexity  : O(n) in worst case (if all elements are the target) — but O(log n) search followed by linear expansion.
#  Space Complexity : O(1) — only pointers used.
# ============================================================

class Solution(object):
    def searchRange(self, nums, target):
        low, high = 0, len(nums)-1
        start = -1
        end = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                start = mid
                end = mid
                while start > 0 and nums[start-1] == target:
                    start -= 1
                while end < len(nums) - 1 and nums[end+1] == target:
                    end += 1
                break
        return [start, end]

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
