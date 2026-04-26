# ============================================================
#  Problem  : Longest Common Prefix
#  Link     : https://leetcode.com/problems/longest-common-prefix/
#  Platform : LeetCode
#  Topic    : Strings
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  Sort the list of strings. The longest common prefix of the entire 
#  list must be a prefix of both the first and last strings in the 
#  sorted list. We only need to compare characters of the first 
#  and last strings until they diverge.
#
#  Example:
#  Input  : ["flower","flow","flight"]
#  Output : "fl"
#
#  Time Complexity  : O(N log N * M) where N is number of strings and M is avg length
#  Space Complexity : O(M) for the result
# ============================================================

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Sorting helps us compare only the two most "different" strings
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        ans = []
        # Compare first and last strings character by character
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ''.join(ans)
            ans.append(first[i])
            
        return ''.join(ans)

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower","flow","flight"]))  # Expected: "fl"
    print(sol.longestCommonPrefix(["dog","racecar","car"]))      # Expected: ""
