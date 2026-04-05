class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numList = {}
        res = []
        for i,val in enumerate(nums):
            diff = target - val
            if diff in numList:
                res =  [numList[diff], i]
            else:
                numList[val] = i
        return res