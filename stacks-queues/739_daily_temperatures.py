# ============================================================
#  Problem  : Daily Temperature
#  Link     : https://leetcode.com/problems/daily-temperatures/description/
#  Platform : LeetCode 
#  Topic    : Stack
#  Difficulty: Medium 
# ============================================================
#
#  Approach:
#  Use a stack to track indices of days still waiting for a warmer temperature. 
#  For each day, if the current temp is warmer than the index on top of the stack, that day found its answer — pop it and store i - prev_index. 
#  Keep popping until the stack is empty or current temp isn't warmer, then push current index.
#  Stack stays in decreasing order of temperatures. 
#  Anything left at the end never got a warmer day → stays 0.
#
#  Example:
#  Input  : temperatures = [73,74,75,71,69,72,76,73]
#  Output : [1,1,4,2,1,1,0,0]
#
#  Time Complexity  : O(n)
#  Space Complexity : O(n)
# ============================================================

class Solution(object):
    def dailyTemperatures(self, temperatures):
        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
            
# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    print(solution())
