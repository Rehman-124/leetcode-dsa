class Solution(object):
    def maxProfit(self, prices):
        lowPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price < lowPrice:
                lowPrice = price

            currentProfit = price - lowPrice

            if currentProfit > maxProfit:
                maxProfit = currentProfit

        return maxProfit