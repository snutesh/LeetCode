class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if len(nums) == 0:
            return
        i = 0
        while(i<len(nums)):
            start = i
            end = i
            while (end+1)<len(nums) and nums[end+1] == (nums[end]+1):
                end = end+1
            if end>start:
                res.append(str(nums[start]) + "->" + str(nums[end]))
            else:
                res.append(str(nums[start]))
            i = end + 1
        return res