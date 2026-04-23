# ============================================================
#  Problem  : 1903. Largest Odd Number in String
#  Link     : https://leetcode.com/problems/largest-odd-number-in-string/
#  Platform : LeetCode
#  Topic    : Strings
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  To find the largest odd number, we need to find the rightmost
#  odd digit. Every substring starting from index 0 and ending 
#  at an odd digit is an odd number. The longest one ends 
#  at the rightmost odd digit.
#
#  Example:
#  Input  : num = "52"
#  Output : "5"
#
#  Time Complexity  : O(n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def largestOddNumber(self, num):
        # Iterate from right to left to find the first odd digit
        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        
        return ""


# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.largestOddNumber("52")) # Expected: "5"
    print(sol.largestOddNumber("4206")) # Expected: ""
    print(sol.largestOddNumber("35427")) # Expected: "35427"
