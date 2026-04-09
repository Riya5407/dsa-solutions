# ============================================================
#  Problem  : 1. Two Sum
#  Link     : https://leetcode.com/problems/two-sum/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. We'll start by taking the first number from the array.
#  2. Then, we'll go through the rest of the numbers one by one.
#  3. If the sum of our first number and any subsequent number equals the target, we've found our pair!
#  4. We'll return the indices of these two numbers as soon as we find them.
#
#  Example:
#  Input  : nums = [2,7,11,15], target = 9
#  Output : [0,1]
#
#  Time Complexity  : O(n^2) — because we're using nested loops, which means checking every possible pair.
#  Space Complexity : O(1) — we're not using any extra space that grows with the input size, just a few variables.
# ============================================================

class Solution(object):
    def twoSum(self, nums, target):
        count = len(nums)
        for i in range(count):
            for j in range(i + 1,count):
                if(nums[i] + nums[j] == target):
                    return [i,j]
                    break

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
