# ============================================================
#  Problem  : 18. 4Sum
#  Link     : https://leetcode.com/problems/4sum/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Sort the input array to handle duplicates easily and use two-pointer technique.
#  2. Use two nested loops to fix the first two elements.
#  3. For the remaining two elements, use a classic two-pointer approach (left and right).
#  4. Skip duplicates to ensure unique quadruplets in the result.
#
#  Example:
#  Input  : nums = [1,0,-1,0,-2,2], target = 0
#  Output : [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#  Time Complexity  : O(n^3) — due to two nested loops and a two-pointer scan.
#  Space Complexity : O(1) — excluding the output list, uses only constant extra space.
# ============================================================

class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return ans

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.fourSum([1,0,-1,0,-2,2], 0))
