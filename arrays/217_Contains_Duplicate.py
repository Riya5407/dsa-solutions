# ============================================================
#  Problem  : 217. Contains Duplicate
#  Link     : https://leetcode.com/problems/contains-duplicate/
#  Platform : LeetCode
#  Topic    : Array / Hash Table
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. Use a set to track numbers we've already seen.
#  2. For each number, check if it's already in the set.
#  3. If yes, we found a duplicate — return True.
#  4. Otherwise, add the number to the set and continue.
#  5. If we finish the loop without finding a duplicate, return False.
#
#  Example:
#  Input  : nums = [1,2,3,1]
#  Output : True
#
#  Time Complexity  : O(n) — single pass through the array
#  Space Complexity : O(n) — set can hold up to n elements
# ============================================================

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,1]))    # True
    print(sol.containsDuplicate([1,2,3,4]))    # False
