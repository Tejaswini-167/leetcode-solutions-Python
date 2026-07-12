class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = maximum = nums[0]

        for num in range(1,len(nums)):
            current = max(nums[num], current + nums[num])
            maximum= max(maximum, current)
        return maximum