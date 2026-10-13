class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        if len(nums) == 3 and sum(nums) != 0:
            return []
        
        nums = sorted(nums)

        i = 0

        op = list()

        while i < len(nums):
            beg = i+1
            end = len(nums) - 1
            while beg < end:
                if nums[i] + nums[beg] + nums[end] == 0:
                    if [nums[i], nums[beg], nums[end]] not in op:
                        op.append([nums[i], nums[beg], nums[end]])
                    beg+=1
                    end-=1
                elif nums[i] + nums[beg] + nums[end] > 0:
                    end-=1
                elif nums[i] + nums[beg] + nums[end] < 0:
                    beg+=1
            i+=1
        return op