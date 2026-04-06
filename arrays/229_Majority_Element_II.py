# ============================================================
#  Problem  : 229. Majority Element II
#  Link     : https://leetcode.com/problems/majority-element-ii/
#  Platform : LeetCode
#  Topic    : Array
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. Use the Boyer-Moore Voting Algorithm to find up to two potential majority elements, since at most two elements can appear more than n/3 times.
#  2. Initialize two candidate elements and their counts. Iterate through the array to find these candidates, incrementing counts if a match, or decrementing both if no match and counts are non-zero.
#  3. After the first pass, reset the counts to zero. Perform a second pass through the array to get the actual counts for the two candidate elements found.
#  4. Finally, check if the actual count for each candidate is greater than n/3. If so, add it to our result list.
#
#  Example:
#  Input  : [1,1,1,3,3,2,2,2]
#  Output : [1,2]
#
#  Time Complexity  : O(n) — We iterate through the array twice.
#  Space Complexity : O(1) — We use a constant amount of extra space for variables.
# ============================================================

class Solution(object):
    def majorityElement(self, nums):
        el1 = None
        el2 = None
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
            elif cnt1 == 0:
                el1 = num
                cnt1 =1
            elif cnt2 == 0:
                el2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
        
        ans = []
        if cnt1 > len(nums)//3:
            ans.append(el1)
        if cnt2 > len(nums)//3:
            ans.append(el2)
        
        return ans
        

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
