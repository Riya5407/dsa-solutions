# ============================================================
#  Problem  : 167. Two Sum II - Input Array Is Sorted
#  Link     : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#  Platform : LeetCode
#  Topic    : Two Pointers
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Start with two pointers: 'left' at the beginning and 'right' at the end of the array.
#  2. While 'left' is less than 'right', calculate the sum of the numbers at these pointers.
#  3. If the sum equals the target, you've found your numbers! Return their 1-indexed positions.
#  4. If the sum is too small, move 'left' one step to the right to try a larger number; if the sum is too large, move 'right' one step to the left to try a smaller number.
#
#  Example:
#  Input  : numbers = [2,7,11,15], target = 9
#  Output : [1,2]
#
#  Time Complexity  : O(n) — The two pointers traverse the array at most once.
#  Space Complexity : O(1) — We only use a few constant extra variables.
# ============================================================

class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers)-1
        while(left<right):
            sum = numbers[left] + numbers[right]
            if(sum == target):
                return [left+1,right+1]
            elif(sum<target):
                left+=1
            else:
                right-=1

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
