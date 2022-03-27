class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        count = {}
        res = []
        for i in range(len(mat)):
            count[i] = mat[i].count(1)
        b = sorted(count, key=count.get)
        for i in range(k):
            res.append(b[i])
        return res