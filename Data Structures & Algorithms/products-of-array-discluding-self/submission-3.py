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
        res = []
        for j in range(len(nums)):
            a = nums[j]
            if zero:
                res.append(0 if a else prod)
            else:
                res.append(prod // a)
        return res