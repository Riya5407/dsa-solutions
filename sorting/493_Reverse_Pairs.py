# ============================================================
#  Problem  : Reverse Pairs
#  Link     : https://leetcode.com/problems/reverse-pairs/
#  Platform : LeetCode
#  Topic    : Sorting
#  Difficulty: Hard
# ============================================================
#
#  Approach:
#  Use a modified merge sort. During the merge step, for each 
#  element in the left half, count how many elements in the 
#  right half satisfy nums[i] > 2 * nums[j]. Because both halves
#  are sorted, we can efficiently count using two pointers.
#
#  Time Complexity  : O(n log n)
#  Space Complexity : O(n)
# ============================================================

class Solution(object):
    def reversePairs(self, nums):
        def mergesort(arr, left, right):
            if left >= right:
                return 0
            mid = (left+right)//2
            count = mergesort(arr,left,mid) + mergesort(arr,mid+1, right)
            j = mid + 1
            for i in range(left,mid+1):
                while j <= right and arr[i] > 2*arr[j]:
                    j += 1
                count += j -(mid+1)
            temp = []
            i, j = left,mid+1
            while i<= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i<=mid:
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1
            arr[left:right+1] = temp
            return count
        return mergesort(nums,0,len(nums)-1)

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.reversePairs([1,3,2,3,1]))
    print("Test 2:", sol.reversePairs([2,4,3,5,1]))
