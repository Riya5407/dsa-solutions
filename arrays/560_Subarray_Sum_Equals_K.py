# ============================================================
#  Problem  : 560. Subarray Sum Equals K
#  Link     : https://leetcode.com/problems/subarray-sum-equals-k/
#  Platform : LeetCode
#  Topic    : Hash Map
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  1. We use a hash map to keep track of the frequency of prefix sums encountered so far.
#  2. Initialize our count of valid subarrays to 0, current prefix sum to 0, and the hash map with `{0: 1}` to handle cases where a subarray starting from index 0 sums to 'k'.
#  3. Iterate through each number in the input array, adding it to the current `prefix_sum`.
#  4. For each `prefix_sum`, check if `prefix_sum - k` exists in our hash map. If it does, add its frequency to our `count` because it means there's a subarray ending here that sums to `k`.
#  5. Finally, update the frequency of the current `prefix_sum` in our hash map.
#
#  Example:
#  Input  : nums = [1,1,1], k = 2
#  Output : 2
#
#  Time Complexity  : O(n) — We iterate through the array once, and hash map operations are O(1) on average.
#  Space Complexity : O(n) — In the worst case, all prefix sums are unique, requiring O(n) space for the hash map.
# ============================================================

class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        freq = {0:1}
        for num in nums:
            prefix_sum += num
            count += freq.get(prefix_sum - k, 0)
            freq[prefix_sum] = freq.get(prefix_sum,0) + 1
        return count
        

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol)
