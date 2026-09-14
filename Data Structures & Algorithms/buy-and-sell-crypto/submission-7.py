class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices) < 2): return 0

        max_value_candidate = 0
        max_value = 0
        current_profit = 0

        for i in range(len(prices) - 1, -1, -1):
            if(prices[i] > max_value_candidate):
                max_value_candidate = prices[i]
            elif(prices[i] < max_value_candidate):
                max_value = max_value_candidate
                if(max_value - prices[i] > current_profit):
                    current_profit = max_value - prices[i]

        return current_profit

