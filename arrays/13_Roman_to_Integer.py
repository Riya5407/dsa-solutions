# ============================================================
#  Problem  : 13. Roman to Integer
#  Link     : https://leetcode.com/problems/roman-to-integer/
#  Platform : LeetCode
#  Topic    : Hash Map
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. First, set up a map that links each Roman numeral character (I, V, X, L, C, D, M) to its integer value.
#  2. Initialize a 'total' variable to keep track of our sum.
#  3. Loop through the input string, checking each character up to the second-to-last one.
#  4. If the current character's value is less than the next one's (like 'I' before 'V'), subtract it from the total; otherwise, add it. Don't forget to add the value of the very last character after the loop!
#
#  Example:
#  Input  : MCMXCIV
#  Output : 1994
#
#  Time Complexity  : O(N) — We iterate through the input string once, where N is the length of the string.
#  Space Complexity : O(1) — The hash map stores a fixed number of Roman numeral characters, not dependent on the input size.
# ============================================================

class Solution(object):
    def romanToInt(self, s):
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s) - 1):
            if roman_map[s[i]] < roman_map[s[i+1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
        total += roman_map[s[-1]]  # Add last character
        return total

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
