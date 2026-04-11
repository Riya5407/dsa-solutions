# ============================================================
#  Problem  : 121. Best Time to Buy and Sell Stock
#  Link     : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#  Platform : LeetCode
#  Topic    : Array / Greedy
#  Difficulty: Easy
# ============================================================
#
#  Approach:
#  1. Track the minimum price seen so far (best day to buy).
#  2. At each price, calculate potential profit = current price - min_price.
#  3. Update max_profit if this profit is better than what we've seen.
#  4. Return max_profit at the end.
#
#  Example:
#  Input  : prices = [7,1,5,3,6,4]
#  Output : 5
#
#  Time Complexity  : O(n) — single pass through the array
#  Space Complexity : O(1) — only two variables used
# ============================================================

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_price = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_price:
                max_price = price - min_price
        return max_price

# ── Quick test ───────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))  # 5
    print(sol.maxProfit([7,6,4,3,1]))    # 0
