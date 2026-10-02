class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        beg = 0
        end = len(nums) - 1

        op = list()

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i] + nums[j] == target:
                    op.append(i)
                    op.append(j)
        return list(set(op))
            
            
