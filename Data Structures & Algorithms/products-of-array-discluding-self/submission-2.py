class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero = 1, 0 
        for i in nums:
            if i:
                prod *= i
            else:
                zero += 1
        if zero > 1:
            return [0] * len(nums)
        res = [0] * len(nums)
        for j in range(len(nums)):
            a = nums[j]
            if zero:
                if a:
                    res[j] = 0
                else:
                    res[j] = prod
            else:
                res[j] = prod // a
        return res