class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = dict() # Create a dictionary
        for index, val in enumerate (nums):
            complement = target - val
            if complement in num:
                return [num[complement], index]
            num[val] = index