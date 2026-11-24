class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}

        def dfsHelper(i, profit, weight, capacity):
            if i >= len(profit):
                return 0

            if (i, capacity) in cache:
                return cache[(i, capacity)]

            # exclude current item
            cache[(i, capacity)] = dfsHelper(i + 1, profit, weight, capacity)

            # include current item
            newCap = capacity - weight[i]
            if newCap >= 0:
                p = profit[i] + dfsHelper(i + 1, profit, weight, newCap)
                cache[(i, capacity)] = max(cache[(i, capacity)], p)

            return cache[(i, capacity)]

        return dfsHelper(0, profit, weight, capacity)