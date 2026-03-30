class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            l,r = i+1 , len(nums) - 1
            while l < r:
                    diff = 0 - val
                    tot = nums[l] + nums[r] 
                    if tot > diff:
                        r -= 1
                    elif tot < diff:
                        l += 1
                    else:
                        res.append([val,nums[l],nums[r]])
                        while l < len(nums)-1 and nums[l] == nums[l+1]:
                            l +=1
                        while r > 0 and nums[r] == nums[r-1]:
                            r -=1
                        l,r = l+1, r-1 
        return res