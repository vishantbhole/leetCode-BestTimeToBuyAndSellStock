class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        
        max_profit = 0
        buy_price = prices[0]
        for i in range(1,length):
            print("buy_price = " + str(buy_price)) 

            if buy_price > prices[i]:
                buy_price = prices[i]
            elif prices[i] - buy_price  > max_profit:
                max_profit = prices[i] - buy_price 
                print("max_profit = " + str(max_profit)) 

        return max_profit
