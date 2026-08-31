class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ls = []
        for i in nums1:
            for j in range(nums2.index(i), len(nums2)):
                if nums2[j] > i:
                    ls.append(nums2[j])
                    break
                if j == len(nums2) - 1 and nums2[j] <= i:
                    ls.append(-1)
        return ls