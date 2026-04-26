# ============================================================
#  Problem  : Rotate String
#  Link     : https://leetcode.com/problems/rotate-string/
#  Platform : LeetCode
#  Topic    : Strings
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  If two strings have different lengths, one cannot be a rotation 
#  of the other. If lengths are equal, we concatenate the string 
#  's' with itself (s + s). If 'goal' is a rotation of 's', it 
#  must be a substring of 's + s'.
#
#  Example:
#  Input  : s = "abcde", goal = "cdeab"
#  Output : true
#
#  Time Complexity  : O(N) where N is the length of the string
#  Space Complexity : O(N) for the concatenated string
# ============================================================

class Solution(object):
    def rotateString(self, s, goal):
        # Base case: lengths must be equal
        if len(s) != len(goal):
            return False
            
        # If 'goal' is a rotation of 's', it will be in 's + s'
        double = s + s
        return goal in double

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.rotateString("abcde", "cdeab"))  # Expected: True
    print(sol.rotateString("abcde", "abced"))  # Expected: False
