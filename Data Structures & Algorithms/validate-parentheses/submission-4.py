class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = "({["
        closing = ")}]"
        for par in s:
            if par in opening:
                stack.append(par)
            else:
                if len(stack) == 0:
                     return False
                else: 
                    if not opening.index(stack.pop()) == closing.index(par):
                        return False
        return len(stack) == 0