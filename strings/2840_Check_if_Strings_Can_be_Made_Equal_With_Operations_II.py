# ============================================================
#  Problem  : Check if Strings Can be Made Equal With Operations II
#  Link     : https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/
#  Platform : LeetCode
#  Topic    : Strings
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  Separately sort the characters at the even indices and odd 
#  indices for both strings. If the sorted versions form identical 
#  collections for both subsets, they can be made equal.
#
#  Time Complexity  : O(n log n)
#  Space Complexity : O(n)
# ============================================================

class Solution(object):
    def checkStrings(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return (sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2]))

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.checkStrings("abcdba", "cabdab"))
