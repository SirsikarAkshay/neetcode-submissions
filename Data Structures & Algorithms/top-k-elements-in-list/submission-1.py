from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)

        for n in nums:
            counts[n] +=1
        
        counts = dict(counts)
        counts = {k: v for k, v in sorted(counts.items(), reverse=True, key=lambda item: item[1])}

        return list(counts.keys())[:k]
