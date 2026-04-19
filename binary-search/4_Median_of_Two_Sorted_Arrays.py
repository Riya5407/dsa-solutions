# ============================================================
#  Problem  : Median of Two Sorted Arrays
#  Link     : https://leetcode.com/problems/median-of-two-sorted-arrays/
#  Platform : LeetCode
#  Topic    : Binary Search
#  Difficulty: Hard
# ============================================================
#
#  Approach:
#  Use binary search on the smaller array to find the correct partition.
#  The cut divides both arrays into left and right halves such that
#  max(left) <= min(right). Since the arrays are sorted, we only need to
#  check the edges of the cuts.
#
#  Time Complexity  : O(log(min(n1, n2)))
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        
        # Ensure nums1 is the smaller array to minimize binary search range
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
            
        low, high = 0, n1
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1
            
            l1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
            r1 = float('inf') if cut1 == n1 else nums1[cut1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]
            
            if l1 <= r2 and l2 <= r1:
                # Found the correct partition
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                # Move partition in nums1 left
                high = cut1 - 1
            else:
                # Move partition in nums1 right
                low = cut1 + 1
        
        return 0.0

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(f"Test 1: {sol.findMedianSortedArrays([1,3], [2])}")    # Expected: 2.0
    print(f"Test 2: {sol.findMedianSortedArrays([1,2], [3,4])}")  # Expected: 2.5
