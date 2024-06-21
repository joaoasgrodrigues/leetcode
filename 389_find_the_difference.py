class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for n in t:
            x = s.replace(n, '',1)
            if len(x) == len(s):
                return n
            else:
                s = x

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        for i in t:
            if s.count(i) != t.count(i):
                return i