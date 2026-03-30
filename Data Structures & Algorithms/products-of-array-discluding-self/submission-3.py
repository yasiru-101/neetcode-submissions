import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_list = []
        for i,val in enumerate(nums):
            if i == 0:
                num_list.append(math.prod(nums[1:]))
            elif i != len(nums):
                num_list.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))
            else:
                num_list.append(math.prod(nums[:-1]))
        return num_list