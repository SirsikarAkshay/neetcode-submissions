class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        high = max(nums)
        low = min(nums)

        n = len(nums)
        act_list = list(range(n+1))

        for i in act_list:
            if i not in nums:
                return i
        