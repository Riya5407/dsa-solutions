# ============================================================
#  Problem  : 136. Single Number
#  Link     : https://leetcode.com/problems/single-number/
#  Platform : LeetCode
#  Topic    : Array / Bit Manipulation
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. Use XOR (^) across all numbers.
#  2. XOR of a number with itself is 0 (a ^ a = 0).
#  3. XOR of a number with 0 is the number itself (a ^ 0 = a).
#  4. Since all duplicates cancel out, only the single number remains.
#
#  Example:
#  Input  : nums = [4,1,2,1,2]
#  Output : 4
#
#  Time Complexity  : O(n) — single pass through the array
#  Space Complexity : O(1) — no extra space used
# ============================================================

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.singleNumber([2,2,1]))      # 1
    print(sol.singleNumber([4,1,2,1,2]))  # 4
