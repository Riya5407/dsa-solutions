# ============================================================
#  Problem  : 49. Group Anagrams
#  Link     : https://leetcode.com/problems/group-anagrams/
#  Platform : LeetCode
#  Topic    : Hash Map
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Initialize a hash map (dictionary) where keys will be sorted strings and values will be lists of anagrams.
#  2. Go through each word in the input list.
#  3. For each word, sort its letters alphabetically to create a unique 'key' representing its anagram group.
#  4. Append the original word to the list associated with its 'key' in our hash map.
#  5. Finally, return all the values (which are the lists of anagrams) from the hash map.
#
#  Example:
#  Input  : ["eat","tea","tan","ate","nat","bat"]
#  Output : [["bat"],["nat","tan"],["ate","eat","tea"]]
#
#  Time Complexity  : O(N * K log K) — where N is the number of strings and K is the maximum length of a string, primarily due to sorting each string.
#  Space Complexity : O(N * K) — for storing all strings in the hash map, where N is the number of strings and K is the maximum length of a string.
# ============================================================

from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
