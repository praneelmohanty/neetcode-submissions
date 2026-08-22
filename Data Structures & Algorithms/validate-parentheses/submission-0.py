class Solution:
    def isValid(self, s: str) -> bool:
        p = {')':'(',']':'[','}':'{'}
        a = []
        for i in s:
            if i in p:
                if not a or a.pop() != p[i]:
                    return False
            else:
                a.append(i)
        return not a