# ============================================================
#  Problem  : 125. Valid Palindrome
#  Link     : https://leetcode.com/problems/valid-palindrome/
#  Platform : LeetCode
#  Topic    : String
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. First, create an empty string to hold only the alphanumeric characters.
#  2. Loop through the input string, checking if each character is alphanumeric. If it is, convert it to lowercase and add it to our new string.
#  3. Next, create a reversed version of this new, cleaned string.
#  4. Finally, compare the cleaned string with its reversed version to see if they are identical.
#
#  Example:
#  Input  : A man, a plan, a canal: Panama
#  Output : true
#
#  Time Complexity  : O(N) — where N is the length of the input string, as we iterate through it once and then create new strings proportional to its length.
#  Space Complexity : O(N) — as we create two new strings, 'clear' and 'rev', which can store up to N characters.
# ============================================================

class Solution(object):
    def isPalindrome(self, s):
        clear = ""
        for i in s:
            if i.isalnum():
                clear += i.lower()
        rev = clear[::-1]
        if rev == clear:
            return True
        else:
            return False

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
