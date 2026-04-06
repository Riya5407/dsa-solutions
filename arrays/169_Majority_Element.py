# ============================================================
#  Problem  : 169. Majority Element
#  Link     : https://leetcode.com/problems/majority-element/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. Initialize a counter to zero and a candidate for the majority element.
#  2. Loop through the array: if the counter is zero, set the current number as the candidate and increment the counter.
#  3. If the current number matches the candidate, increment the counter; otherwise, decrement it.
#  4. After the first loop, the candidate is a potential majority element. Perform a final count to confirm it truly appears more than n/2 times.
#
#  Example:
#  Input  : [2,2,1,1,1,2,2]
#  Output : 2
#
#  Time Complexity  : O(N) — We iterate through the array twice: once to find the candidate and once to count its occurrences.
#  Space Complexity : O(1) — We only use a few constant extra variables.
# ============================================================

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        el = 0
        n = len(nums)
        for num in nums:
            if count == 0:
                el = num
                count += 1
            elif num == el:
                count += 1
            else:
                count -= 1
        cnt1 = nums.count(el)
        if cnt1 > (n//2):
            return el

        return -1
        

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
