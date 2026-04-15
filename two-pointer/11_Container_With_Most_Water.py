# ============================================================
#  Problem  : Container With Most Water
#  Link     : https://leetcode.com/problems/container-with-most-water/
#  Platform : LeetCode
#  Topic    : Two Pointer
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  Use a two-pointer approach starting from both ends. Calculate
#  the volume of water between the pointers, update the max_vol,
#  and logically move the pointer corresponding to the shorter height
#  inward to find a potentially taller container.
#
#  Time Complexity  : O(n)
#  Space Complexity : O(1)
# ============================================================

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_vol = 0
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            vol = h * w
            max_vol = max(vol, max_vol)
            if height[left] < height[right]:
                left += 1
            else:        
                right -= 1
        return max_vol

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Test 1:", sol.maxArea([1,8,6,2,5,4,8,3,7]))
