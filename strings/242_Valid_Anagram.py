# ============================================================
#  Problem  : 242. Valid Anagram
#  Link     : https://leetcode.com/problems/valid-anagram/
#  Platform : LeetCode
#  Topic    : Hash Map
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. First, quickly check if the lengths of the two strings are different; if so, they can't be anagrams.
#  2. Initialize a hash map (or dictionary) to keep track of character counts.
#  3. Go through the first string, incrementing the count for each character in our map, then go through the second string, decrementing counts.
#  4. Finally, check if all the counts in the map are zero. If even one count is not zero, they're not anagrams!
#
#  Example:
#  Input  : s = "anagram", t = "nagaram"
#  Output : true
#
#  Time Complexity  : O(N) — We iterate through both strings once, and then iterate through the map which has at most K (alphabet size) entries.
#  Space Complexity : O(K) — The hash map stores counts for at most K unique characters (where K is the size of the alphabet, typically 26 for English lowercase letters).
# ============================================================

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count = {}

        for char in s:
            count[char] = count.get(char, 0) +1

        for char in t:
            count[char] = count.get(char, 0) -1

        for value in count.values():
            if value != 0:
                return False
        
        return True

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
