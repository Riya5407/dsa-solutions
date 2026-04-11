# ============================================================
#  Problem  : 9. Palindrome Number
#  Link     : https://leetcode.com/problems/palindrome-number/
#  Platform : LeetCode
#  Topic    : Array / Math
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. Negative numbers are never palindromes — return False immediately.
#  2. Reverse the number mathematically by extracting digits one by one.
#  3. Compare the reversed number with the original.
#  4. If they are equal, it's a palindrome.
#
#  Example:
#  Input  : x = 121
#  Output : True
#
#  Time Complexity  : O(log n) — we process each digit once
#  Space Complexity : O(1) — only a few variables used
# ============================================================

class Solution(object):
    def isPalindrome(self, x):
        m = x
        original = m
        rev = 0
        if(original<0):
            return False
        while(m>0):
            digit = m%10
            rev = rev*10 + digit
            m = m//10
        print(rev)
        if(rev==original):
            return True
        else:
            return False

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))   # True
    print(sol.isPalindrome(-121))  # False
    print(sol.isPalindrome(10))    # False
