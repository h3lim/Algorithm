class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minStock = inf
        maxStock = 0
        for i in prices:
            minStock = min(minStock, i)
            maxStock = max(maxStock, i - minStock)

        return maxStock