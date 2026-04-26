# ============================================================
#  Problem  : Isomorphic Strings
#  Link     : https://leetcode.com/problems/isomorphic-strings/
#  Platform : LeetCode
#  Topic    : Strings / Hashing
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  Two strings are isomorphic if the characters in 's' can be replaced 
#  to get 't'. We use two arrays to track the last seen index of each 
#  character in both strings. If the last seen indices don't match 
#  at any position, the strings are not isomorphic.
#
#  Example:
#  Input  : s = "egg", t = "add"
#  Output : true
#
#  Time Complexity  : O(N) where N is the length of the string
#  Space Complexity : O(1) as the character set is fixed (256 ASCII)
# ============================================================

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
            
        n = len(s)
        # Store last seen position + 1 of characters in s and t
        m1, m2 = [0]*256, [0]*256
        
        for i in range(n):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            
            # Use i + 1 because 0 is our initial value indicating "not seen"
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1
            
        return True

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))      # Expected: True
    print(sol.isIsomorphic("foo", "bar"))      # Expected: False
    print(sol.isIsomorphic("paper", "title"))  # Expected: True
