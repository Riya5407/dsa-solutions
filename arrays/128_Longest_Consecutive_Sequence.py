# ============================================================
#  Problem  : 128Longest Consecutive Sequence
#  Platform : LeetCode 
#  Topic    : Arrays 
#  Difficulty: Medium 
# ============================================================
#
#  Approach:
#  1. Convert List into set for simplifying
#  2. Run a loop through set, if element - 1 doesn't exist, then take that element as starting point of subarray
#  3. Run another loop until el - 1 exist in set, increase count and element accordingly
#  4. Also maintain a variable longest to maintain the maximum count occured.
#
#  Example:
#  Input  : nums = [100,4,200,1,3,2]
#  Output : 4
#
#  Time Complexity  : O(n)
#  Space Complexity : O(n)
# ============================================================

class Solution(object):
    def longestConsecutive(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        
        longest = 0
        st1 = set()
        for i in range(n):
            st1.add(nums[i])
        for el in st1:
            if el - 1 not in st1:
                count = 1
                x = el

                while x + 1 in st1:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    print(solution())
