class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_signal = prices[0]
        profit = 0

        for num in range(1,len(prices)):
            if prices[num] <= buy_signal:
                buy_signal = prices[num]
            else :
                temp_profit = prices[num] - buy_signal 
                profit = max(temp_profit, profit)

            
        return profit

        