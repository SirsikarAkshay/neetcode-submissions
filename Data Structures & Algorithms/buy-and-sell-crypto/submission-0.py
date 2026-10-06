class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                t_prof = prices[j] - prices[i] 
                if t_prof > prof:
                    prof = t_prof
        return prof 