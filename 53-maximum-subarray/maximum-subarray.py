class Solution(object):
    def maxSubArray(self, nums):


        """
        :type nums: List[int]
        :rtype: int
        """

        current = maximum = nums[0]

        for n in range(1,len(nums)):
            current = max(current + nums[n], nums[n])
            maximum = max(current,maximum)

        return maximum





