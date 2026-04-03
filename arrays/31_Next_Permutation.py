# ============================================================
#  Problem  : 31_Next_Permutation
#  Platform : LeetCode 
#  Topic    : Arrays 
#  Difficulty: Medium 
# ============================================================
#
#  Approach:
#  1. Run a loop from sequence until you find a pivot point(where the next element is greater than it.)
#  2. If such element exist, then run another reverse loop in sequence until you find an element less thn it(store it's index).
#  3. Swap that two elements to create the smallest next Permutaion
#  4. Then reverse the rest of the list(after the pivot point), and return the edited list
#
#  Example:
#  Input  : nums = [1,2,3]
#  Output : [1,3,2]
#
#  Time Complexity  : O(n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def nextPermutation(self, nums):

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[j], nums[i] = nums[i], nums[j]
        nums[i+1:] = reversed(nums[i+1:])
        return nums
        
# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    print(solution())
