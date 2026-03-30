# ============================================================
#  Problem  : 3Sum
#  Link     : https://leetcode.com/problems/3sum/description/
#  Platform : LeetCode
#  Topic    : Arrays 
#  Difficulty: Medium 
# ============================================================
#
#  Approach:
#  1. Firstly we will sort the list
#  2. Then while traversing a whole list:
#  3. Select an element and then run another loop from next to element's index upto lat element:
#  4. Use left and right  pointer with left initialized from next element of selected element and right from last element
#  5. if the sum of 3 elements is equal to zero then we will add the sorted form of 3 element in result.
#
#  Example:
#  Input  : [-1,0,1,2,-1,-4]
#  Output : [[-1,-1,2],[-1,0,1]]
#
#  Time Complexity  : O(n^2)
#  Space Complexity : O(n)
# ============================================================

class Solution(object):
    def threeSum(self, nums):
        l1 = sorted(nums)
        result = []
        for i in range(len(l1)-1):
            x = l1[i]
            if i > 0 and l1[i]==l1[i-1]:
                continue
            left = i+1
            right = len(l1)-1
            while left < right:
                y = l1[left]
                z = l1[right]
                if x+y+z == 0:
                    result.append([x,y,z])
                    right -= 1
                    left+=1
                elif x+y+z < 0:
                    left += 1
                else:
                    right -= 1
        final = []
        for i in result:
            sorted_i = sorted(i)
            if sorted_i not in final:
                final.append(sorted_i)

        return(final)

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    print(solution())
