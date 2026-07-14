class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        maximum = 0

        for price in prices:
            if price < buy:
                buy = price
            
            if price - buy > maximum:
                maximum = max(maximum, price - buy)

        return maximum