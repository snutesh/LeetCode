class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        n = len(columnTitle)
        for i in range(n):
            num += pow(26, n-i-1)*(ord(columnTitle[i])-ord("A")+1)
        return num