class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums:List[int] means nums is expected to be a list with integers
        num = {} #Create an empty dict
        for i in nums: #Check in the list
            if i in num: #Look if that number is in dict
                return True
            num[i] = True #If number isn't there,write it on dict
        return False #Return false if no duplicates available

        
