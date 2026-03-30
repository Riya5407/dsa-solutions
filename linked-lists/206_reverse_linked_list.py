# ============================================================
#  Problem  : Reerse Linked List
#  Link     : https://leetcode.com/problems/reverse-linked-list/description/
#  Platform : LeetCode 
#  Topic    : Linked List
#  Difficulty: Easy 
# ============================================================
#
#  Approach:
#  1. Traverse through whole Linked List.
#  2. Maintain a nxt pointer, pointing next element of save
#  3. Link the prev to the link part of save
#  4. Move prev to save and save to nxt.
#  5. At last the whole linkedlist will be reversed, return prev
#
#  Example:
#  Input  : head = 1 -> 2 -> 3 -> 4 -> 5
#  Output : 5 -> 4 -> 3 -> 2 -> 1
#
#  Time Complexity  : O(n)
#  Space Complexity : O(1)
# ============================================================

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        save = head
        while save is not None:
            nxt = save.next
            save.next = prev
            prev = save
            save = nxt
        return prev

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    print(solution())
