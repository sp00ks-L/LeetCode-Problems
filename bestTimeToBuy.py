class Solution:
    def buyStock(self, prices):
        """
        Given an array of prices, maximise profit by buying low and selling high
        :param prices: List[int]        [7,1,5,3,6,4]
        :return: int                    7
        """
        profit_sum = 0
        n = len(prices)

        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit_sum += (prices[i] - prices[i - 1])

        return profit_sum


