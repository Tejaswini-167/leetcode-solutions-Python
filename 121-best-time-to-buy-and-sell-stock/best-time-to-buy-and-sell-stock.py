class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        mimimum = prices[0]

        maximum = 0

        for price in prices:
            mimimum = min(mimimum,price)
            maximum = max(maximum, price - mimimum)
            
        return maximum

    