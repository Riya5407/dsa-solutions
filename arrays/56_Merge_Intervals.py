# ============================================================
#  Problem  : 56. Merge Intervals
#  Link     : https://leetcode.com/problems/merge-intervals/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. First, sort the intervals based on their start times.
#  2. Iterate through the sorted intervals.
#  3. If the current interval overlaps with the last merged interval (i.e., current start <= last end), merge them by updating the end time of the last interval.
#  4. Otherwise, add the current interval to the list of merged intervals.
#
#  Example:
#  Input  : intervals = [[1,3],[2,6],[8,10],[15,18]]
#  Output : [[1,6],[8,10],[15,18]]
#
#  Time Complexity  : O(n log n) — due to sorting the intervals.
#  Space Complexity : O(n) — for storing the merged intervals in the result list.
# ============================================================

class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        ans = []
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
