class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0

        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]
            
            if profit < 0 and l != r - 1:
                l += 1
            elif profit < 0 and l == r - 1:
                r += 1
                l += 1
            elif profit > 0 and profit < highest:
                r += 1
            else:
                highest = max(highest, profit)
                r += 1

        return highest
