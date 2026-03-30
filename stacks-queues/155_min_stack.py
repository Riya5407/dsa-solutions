# ============================================================
#  Problem  : Min Stack
#  Link     : https://leetcode.com/problems/min-stack/description/
#  Platform : LeetCode 
#  Topic    : Stack
#  Difficulty: Medium 
# ============================================================
#
#  Approach:
#  1. For push -> Simply append the element in stack
#  2. For pop -> Simply pop the last element
#  3. For Top -> Return the last element stack[-1]
#  4. For getMin -> We will maintain another mini_stack, 
#                   in which whenever we will append the element:
#                          if that element is less than the last element of the mini_stack
#                   pop the elemenet:
#                          if the pop element from the stack is the last element in the mini_stack
#
#  Example:
#  Input  : ["MinStack","push","push","push","getMin","pop","top","getMin"]
#           [[],[-2],[0],[-3],[],[],[],[]]
#  Output : [null,null,null,null,-3,null,0,-2]
#
#  Time Complexity  : O(1)
#  Space Complexity : O(n) for stack
# ============================================================

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.mini_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.mini_stack or val <= self.mini_stack[-1]:
            self.mini_stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.mini_stack[-1]==self.stack[-1]:
            self.mini_stack.pop()
        self.stack.pop()


        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mini_stack[-1]
        
# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    print(solution())
