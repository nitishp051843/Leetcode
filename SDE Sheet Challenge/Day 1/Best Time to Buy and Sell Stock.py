# Solution 1 - Two Pointer
# Time : O(n)
# Space : O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        fptr = 0
        sptr = 1
        while sptr < len(prices):
            curr_max = prices[sptr] - prices[fptr]
            if curr_max > max_profit:
                max_profit = curr_max

            if prices[fptr] >= prices[sptr]:
                fptr = sptr
            sptr += 1
        return max_profit