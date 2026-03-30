# ============================================================
#  Problem  : Decode String
#  Link     : https://leetcode.com/problems/decode-string/
#  Platform : LeetCode
#  Topic    : Stack 
#  Difficulty: Medium 
# ============================================================
#
#  Approach:
#  Maintain a stack on numbers and char.
#  if “]” → Pop out the stack until “[” while saving the char in temp
#  then pop out the num
#  Then append(num*temp) to final result string
#  return whole joined string
#
#  Example:
#  Input  : s = "3[a]2[bc]"
#  Output : "aaabcbc"
#
#  Time Complexity  : O(n)
#  Space Complexity : O(n)
# ============================================================

class Solution(object):
    def decodeString(self, s):
        res = ""
        stack = []
        for i in s:
            if i != "]":
                stack.append(i)
            else:
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*temp)
        res = "".join(stack)
        return res        

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    print(solution())
