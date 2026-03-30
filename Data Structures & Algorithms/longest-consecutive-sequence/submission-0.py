class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        ordered_list = sorted(list(set(nums)))
        longest = 1
        streak = 1
        for i in range(len(ordered_list) - 1):
            if ordered_list[i] + 1 == ordered_list[i+1]:
                streak += 1
            else:
                streak = 1
            if streak > longest:
                longest = streak
        return longest