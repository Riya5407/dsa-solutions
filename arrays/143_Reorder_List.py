# ============================================================
#  Problem  : 143. Reorder List
#  Link     : https://leetcode.com/problems/reorder-list/
#  Platform : LeetCode
#  Topic    : Linked List
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. First, we'll find the middle of the linked list using the classic slow and fast pointer trick.
#  2. Then, we'll split the list into two halves and reverse the second half of the list.
#  3. Finally, we'll interleave the nodes from the first half and the reversed second half, alternating between them to form the reordered list.
#
#  Example:
#  Input  : [1,2,3,4,5]
#  Output : [1,5,2,4,3]
#
#  Time Complexity  : O(N) — We traverse the list multiple times: once to find the middle, once to reverse the second half, and once to merge the two halves. Each traversal is proportional to the number of nodes N.
#  Space Complexity : O(1) — We only use a few extra pointers for finding the middle, reversing, and merging, so the space used is constant.
# ============================================================

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next

            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        return head

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
