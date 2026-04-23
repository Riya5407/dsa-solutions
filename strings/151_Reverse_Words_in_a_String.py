# ============================================================
#  Problem  : 151. Reverse Words in a String
#  Link     : https://leetcode.com/problems/reverse-words-in-a-string/
#  Platform : LeetCode
#  Topic    : Strings
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  Split the input string into a list of words. The split()
#  method naturally handles multiple spaces between words. 
#  Reverse the list and join the words back into a single 
#  string with single spaces.
#
#  Example:
#  Input  : s = "the sky is blue"
#  Output : "blue is sky the"
#
#  Time Complexity  : O(n)
#  Space Complexity : O(n)
# ============================================================

class Solution(object):
    def reverseWords(self, s):
        # split() handles any amount of whitespace
        words = s.split()
        # Reverse the list of words in-place
        words.reverse()
        # Join with a single space
        return " ".join(words)


# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("the sky is blue")) # Expected: "blue is sky the"
    print(sol.reverseWords("  hello world  ")) # Expected: "world hello"
    print(sol.reverseWords("a good   example")) # Expected: "example good a"
