class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = cntG = cntL = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                cntG = cntL = 1
            elif nums[i - 1] < nums[i]:
                cntG, cntL = cntG + 1, 1
            else:
                cntG, cntL = 1, cntL + 1
            res = max(res, cntG, cntL)
        return res