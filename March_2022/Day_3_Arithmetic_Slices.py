class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        dp = [0]*n
        for i in range(2, n):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = 1 + dp[i-1]
                count = count + dp[i]
        return count