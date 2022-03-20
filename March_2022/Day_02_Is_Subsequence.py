class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sf = 0
        sl = len(s)
        tf = 0
        tl = len(t)
        if len(s) == 0:
            return True
        while(sf != sl and tf != tl):
            if s[sf] == t[tf]:
                sf = sf + 1
                tf = tf + 1
            else:
                tf = tf + 1
        if sf == sl:
            return True
        else:
            return False