class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        if len(nums) == 3 and sum(nums) != 0:
            return []
        
        nums = sorted(nums)
        l = len(nums)

        final_list = list()

        i = 0
        while i < l:

            p1 = i + 1
            p2 = l - 1
            
            while p1 < p2:
                op_list = list()
                if nums[i] + nums[p1] + nums[p2] == 0:
                    op_list.append(nums[i])
                    op_list.append(nums[p1])
                    op_list.append(nums[p2])
                    if len(op_list) > 0 and op_list not in final_list:
                        final_list.append(op_list)
                    p1+=1
                    continue
                if nums[i] + nums[p1] + nums[p2] == 0:
                    op_list.append(nums[i])
                    op_list.append(nums[p1])
                    op_list.append(nums[p2])
                    if len(op_list) > 0 and op_list not in final_list:
                        final_list.append(op_list)
                    p2-=1
                    continue
                if nums[i] + nums[p1] + nums[p2] > 0:
                    p2-=1
                    continue
                if nums[i] + nums[p1] + nums[p2] > 0:
                    p1+=1 
                    continue
                p1+=1
                continue
                p2-=1
                continue
            i+=1
                
        return final_list
 



            