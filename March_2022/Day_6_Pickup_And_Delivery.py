class Solution:
    def countOrders(self, n: int) -> int:
        s = 1
        for i in range(1,n+1):
            s *= i * (2 * i - 1)
            s %= 1000000007
        return s