class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        f = [-1]* (n+1)
        f[0] = 1
        f[1] = 2

        i = 2
        while i <= n:
            f[i] = f[i-1]+f[i-2]
            i+=1

        return f[n-1]
