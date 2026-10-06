class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [amount+1]*(amount+1)
        f[0] = 0

        lf = len(f)
        for i in range(1, lf):
            for c in coins:
                if i-c >= 0:
                    f[i] = min(f[i], f[i-c]+1)

        if f[amount] > amount:
            return -1
        else:
            return f[amount]



        
