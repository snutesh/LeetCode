class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0]*10001
        for i in nums:
            dp[i] += i
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i]+dp[i-2])
        return dp[10000]