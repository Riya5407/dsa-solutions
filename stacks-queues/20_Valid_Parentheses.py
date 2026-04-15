# ============================================================
#  Problem  : Valid Parentheses
#  Link     : https://leetcode.com/problems/valid-parentheses/
#  Platform : LeetCode
#  Topic    : Stacks & Queues
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  Use a stack to keep track of opening brackets. When a closing
#  bracket is encountered, check if it matches the top of the
#  stack. If it does, pop from the stack. Otherwise, return False.
#
#  Time Complexity  : O(n)
#  Space Complexity : O(n)
# ============================================================

class Solution(object):
    def isValid(self, s):
        stack = []
        top = 0
        for i in range(0,len(s)):
            top += 1
            x = s[i]
            stack.append(x)
            if(x == ")"):
                while(stack[top]=="("):
                    stack.pop()
            if(x == "}"):
                while(stack[top]=="{"):
                    stack.pop()
            if(x == "]"):
                while(stack[top]=="["):
                    stack.pop()
        if(top==0):
            return True
        else:
            return False

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.isValid("()"))
    print("Test 2:", sol.isValid("()[]{}"))
