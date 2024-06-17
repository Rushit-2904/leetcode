from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for sell_price in prices[1:]:
            if buy_price > sell_price:
                buy_price = sell_price
            profit = max(profit,sell_price - buy_price)
        return profit