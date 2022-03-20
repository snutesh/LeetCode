class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            binr = bin(i)
            strs = str(binr)
            count = strs.count("1")
            ans.append(count)
        return ans