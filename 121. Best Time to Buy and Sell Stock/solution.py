class Solution:
    def maxProfit(self, prices:List[int]) -> int:
        n = len(prices)
        if not prices : return 0
        maxProfit = 0
        minBuy = prices[0]

        for i in range(1, n):
            sell = prices[i]
            profit = sell - minBuy
            maxProfit = max(maxProfit, profit)
            minBuy = min(minBuy, prices[i])
        
        return maxProfit
        #MaxProfit 