class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        LeftPoint=0
        RightPoint=1
        maxP=0

        while RightPoint<len(prices):
            if prices[LeftPoint] < prices[RightPoint]:
                profit=prices[RightPoint] - prices[LeftPoint]
                maxP=max(maxP, profit)
            else:
                LeftPoint=RightPoint
            RightPoint+=1
        
        return maxP