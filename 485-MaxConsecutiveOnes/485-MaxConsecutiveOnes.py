class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 =0
        ctr = 0
        for i in range(len(nums)):
            if nums[i] ==1 :
                ctr+=1
                max1 = max(max1,ctr)
            else:
                ctr = 0
        return max1