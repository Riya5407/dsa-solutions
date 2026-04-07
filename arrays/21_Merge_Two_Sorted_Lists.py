# ============================================================
#  Problem  : 21. Merge Two Sorted Lists
#  Link     : https://leetcode.com/problems/merge-two-sorted-lists/
#  Platform : LeetCode
#  Topic    : Linked List
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. First, handle the base cases where one or both lists might be empty.
#  2. Determine the head of the merged list by comparing the first nodes and assigning the smaller one.
#  3. Iterate through both lists, at each step, attach the node with the smaller value to the `next` of the `prev` node, then advance the `prev` pointer and the pointer of the list from which the node was taken.
#  4. Once one list is exhausted, simply append the remaining nodes of the other list to the end of the merged list.
#
#  Example:
#  Input  : list1 = [1,2,4], list2 = [1,3,4]
#  Output : [1,1,2,3,4,4]
#
#  Time Complexity  : O(m + n) — where m and n are the lengths of list1 and list2, as we traverse each list at most once.
#  Space Complexity : O(1) — we only use a few extra pointers, so the space complexity is constant.
# ============================================================

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        prev = head
        first = list1
        second = list2
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1:
            prev.next = list1
        else:
            prev.next = list2

        return head

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
