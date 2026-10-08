class Solution:
    def countBits(self, n: int) -> List[int]:

        bits = [bin(i) for i in range(n+1)]
        counts = [bit.count("1") for bit in bits]

        return counts