# ============================================================
#  Problem  : Two Sum II - Input Array Is Sorted
#  Link     : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#  Platform : LeetCode 167
#  Topic    : Two Pointer
#  Difficulty: Medium
# ============================================================
#
#  Approach:
#  Since the array is already sorted, use two pointers — one at
#  the start (left) and one at the end (right). If their sum is
#  too big, move right inward. If too small, move left outward.
#  Guaranteed to find exactly one solution.
#
#  Example:
#  Input  : numbers = [2, 7, 11, 15], target = 9
#  Output : [1, 2]   (1-indexed)
#
#  Time Complexity  : O(n)
#  Space Complexity : O(1)
# ============================================================

def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        current_sum = numbers[l] + numbers[r]

        if current_sum == target:
            return [l + 1, r + 1]
        elif current_sum < target:
            l += 1
        else:
            r -= 1

    return []


# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))    # Expected: [1, 2]
    print(twoSum([2, 3, 4], 6))         # Expected: [1, 3]
    print(twoSum([-1, 0], -1))          # Expected: [1, 2]
