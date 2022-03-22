class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ['a']*n
        k = k - n
        i = n - 1
        while k:
            k = k + 1
            if k/26 >=1:
                result[i] = 'z'
                k = k - 26
                i = i-1
            else:
                result[i] = chr(k + 96)
                k = 0
        return "".join(result)