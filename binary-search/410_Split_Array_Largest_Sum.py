# ============================================================
#  Problem  : Split Array Largest Sum
#  Link     : https://leetcode.com/problems/split-array-largest-sum/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Hard
# ============================================================
#
#  Approach:
#  This is another binary search on answer problem. The minimum possible answer
#  is the maximum element in the array (if we split into N subarrays), and the
#  maximum answer is the sum of the array (if k=1). We binary search for the
#  maximum subarray sum and count how many partitions are required for that sum.
#
#  Time Complexity  : O(N * log(Sum - Max))
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def is_possible(self, nums, mid, k):
        partitions = 1
        current_sum = 0
        for i in range(len(nums)):
            if current_sum + nums[i] <= mid:
                current_sum += nums[i]
            else:
                partitions += 1
                current_sum = nums[i]
        return partitions
    
    def splitArray(self, nums, k):
        low, high = max(nums), sum(nums)
        while low <= high:
            mid = (low+high)//2
            partitions = self.is_possible(nums, mid, k)
            if partitions <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low
        
# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    solution = Solution()
    print(solution.splitArray([7,2,5,10,8], 2)) # Expected: 18
