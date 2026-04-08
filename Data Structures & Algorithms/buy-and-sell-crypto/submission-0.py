class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            max_profit = max(max_profit,abs(prices[left]-prices[right]))
        return max_profit
