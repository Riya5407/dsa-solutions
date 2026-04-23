# ============================================================
#  Problem  : 1021. Remove Outermost Parentheses
#  Link     : https://leetcode.com/problems/remove-outermost-parentheses/
#  Platform : LeetCode
#  Topic    : Stacks & Queues
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  Use a counter to track the nesting 'level'. Every '(' 
#  increments the level and every ')' decrements it. 
#  A '(' is outermost if level is 0 before incrementing.
#  A ')' is outermost if level is 1 before decrementing.
#  We only include brackets that are NOT outermost.
#
#  Example:
#  Input  : s = "(()())(())"
#  Output : "()()()"
#
#  Time Complexity  : O(n)
#  Space Complexity : O(n)
# ============================================================

class Solution(object):
    def removeOuterParentheses(self, s):
        res = ""
        level = 0           

        for char in s:
            if char == '(':
                # If level > 0, it means it's already inside 
                # an outermost parenthesis
                if level > 0:
                    res += char
                level += 1
            elif char == ')':
                level -= 1
                # If level > 0 after decrementing, it means 
                # we are still inside an outermost parenthesis
                if level > 0:
                    res += char

        return res


# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.removeOuterParentheses("(()())(())")) # Expected: "()()()"
    print(sol.removeOuterParentheses("(()())(())(()(()))")) # Expected: "()()()()(())"
    print(sol.removeOuterParentheses("()()")) # Expected: ""
