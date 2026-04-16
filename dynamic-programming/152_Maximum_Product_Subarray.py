# ============================================================
#  Problem  : Maximum Product Subarray
#  Link     : https://leetcode.com/problems/maximum-product-subarray/
#  Platform : LeetCode
#  Topic    : Dynamic Programming
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  Maintain the running max product and min product because 
#  multiplying a negative value can flip the signs and turn a 
#  minimum into a maximum and vice versa.
#
#  Time Complexity  : O(n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def maxProduct(self, nums):
        res = nums[0]
        maxprod = nums[0]
        minprod = nums[0]

        for i in range(1,len(nums)):
            curr = nums[i]
            if curr < 0:
                maxprod, minprod = minprod,maxprod

            maxprod = max(curr, maxprod*curr)
            minprod = min(curr, minprod*curr)

            res = max(res, maxprod)
        return res

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.maxProduct([2,3,-2,4]))
