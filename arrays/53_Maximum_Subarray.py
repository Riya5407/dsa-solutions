# ============================================================
#  Problem  : 53 Maximum Subarray
#  Platform : LeetCode 
#  Topic    : Arrays 
#  Difficulty: Medium 
# ============================================================
#
#  Approach:
#  1. Run a loop through the list, add the element in sum
#  2. If sum becomes 0, reset sum to 0
#  3. Maintain a variable to track the maximum sum occured until now.
#  4. Atlast return maximum sum
#
#  Example:
#  Input  : nums = [-2,1,-3,4,-1,2,1,-5,4]
#  Output : 6
#
#  Time Complexity  : O(n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def maxSubArray(self, nums):
        maxi = float('-inf')
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum > maxi:
                maxi = sum
            if sum < 0:
                sum = 0
        return maxi

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    print(solution())
