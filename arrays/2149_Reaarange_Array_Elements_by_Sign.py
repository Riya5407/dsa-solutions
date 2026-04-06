# ============================================================
#  Problem  : 2149. Rearrange Array Elements by Sign
#  Link     : https://leetcode.com/problems/rearrange-array-elements-by-sign/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Create a new `result` array of the same length as the input, initialized with zeros.
#  2. Initialize two pointers: `pos` at index 0 for positive numbers and `neg` at index 1 for negative numbers.
#  3. Iterate through each number in the input `nums` array.
#  4. If the number is positive, place it at `result[pos]` and increment `pos` by 2. If it's negative, place it at `result[neg]` and increment `neg` by 2.
#
#  Example:
#  Input  : [3,1,-2,-5,2,-4]
#  Output : [3,-2,1,-5,2,-4]
#
#  Time Complexity  : O(n) — We iterate through the input array once.
#  Space Complexity : O(n) — We create a new array of the same size to store the result.
# ============================================================

class Solution(object):
    def rearrangeArray(self, nums):
        result = [0]  * len(nums)
        pos = 0
        neg = 1
        for num in nums:
            if num < 0:
                result[neg] = num
                neg += 2
            elif num > 0:
                result[pos] = num
                pos += 2
        return result
        

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
