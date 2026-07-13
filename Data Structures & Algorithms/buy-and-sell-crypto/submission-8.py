class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0 
        n = len(prices)

        min_prices = prices[0]

        for i in range(n):
            min_prices = min(min_prices, prices[i])
            curr_diff = prices[i] - min_prices
            max_diff = max(max_diff, curr_diff)
        

        return max_diff


        ##min_prices = 10; min_prices = 10, curr_diff = 0, max_diff = 0
        ## min_prices = 1, curr_diff = 0, max_diff = 0
        ##min_prices = 1, curr_diff = 5 - 1 = 4, max_diff = 4
        ##...
        ##min_prices = 1, curr_diff = 7 - 1 =6, max_diff = 6
        
            
        
        
