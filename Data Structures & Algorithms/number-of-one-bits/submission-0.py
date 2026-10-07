class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)

        count = 0
        for s in b:
            if s == "1":
                count+=1
        return count