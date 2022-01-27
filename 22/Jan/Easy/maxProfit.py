#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit_1(self, prices: List[int]) -> int:
        max_profit = 0
        length = len(prices)
        for index, value in enumerate(prices):
            if index+1 < length:
                for j in prices[index:]:
                    temp = j - prices[index]
                    #print(temp, max_profit)
                    if temp > max_profit:
                        max_profit = temp
        return max_profit
    
    def maxProfit(self, prices: List[int]) -> int:
        cost = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            cost = min(cost, prices[i])
            profit = max(profit, prices[i] - cost)
        return profit
            
        