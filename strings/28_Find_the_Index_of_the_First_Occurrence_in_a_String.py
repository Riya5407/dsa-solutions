# ============================================================
#  Problem  : Find the Index of the First Occurrence in a String
#  Link     : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
#  Platform : LeetCode
#  Topic    : Strings
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  Check all substrings in the haystack of the needle's length. 
#  If an exact match is found, return the starting index.
#
#  Time Complexity  : O(m * n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def strStr(self, haystack, needle):
        m = len(haystack)
        n = len(needle)
        for i in range(m-n+1):
            if(haystack[i:i+n] == needle):
                return i
        if(m==n==1):
            if(haystack==needle):
                return 0
        return -1

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.strStr("sadbutsad", "sad"))
