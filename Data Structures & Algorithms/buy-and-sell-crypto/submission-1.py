class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for i in prices:
            buy = min(buy, i)
            maxProfit = max(maxProfit, i - buy)
        return maxProfit