// Last updated: 13/02/2025, 21:16:43
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range (0,len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
        