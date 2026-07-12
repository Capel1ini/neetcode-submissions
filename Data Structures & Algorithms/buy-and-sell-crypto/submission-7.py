class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = l + 1
        Profit = 0
        while r < len(prices):
            Profit = max(Profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l, r = r, r + 1 
            else:
                r = r + 1
        return Profit

                

        

        