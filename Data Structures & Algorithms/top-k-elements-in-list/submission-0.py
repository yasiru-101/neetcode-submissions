class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = {}
        number_list = []
        for i,val in enumerate(nums):
            if val in num:
                num[val] += 1
            else:
                num[val] = 1
        sorted_data = dict(sorted(num.items(),key = lambda item: item[1], reverse = True))
        numbered_list = list(sorted_data.keys())
        return numbered_list[:k]