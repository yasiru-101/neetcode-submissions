class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char1 in s:
            if char1 in s_dict:
                s_dict[char1]+=1
            else:
                s_dict[char1] =1
        for char2 in t:
            if char2 in t_dict:
                t_dict[char2]+=1
            else:
                t_dict[char2] = 1
        return s_dict == t_dict
        