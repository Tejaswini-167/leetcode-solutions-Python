class Solution(object):
    def maxSubArray(self, nums):

        current = maximum = nums[0]
        

        for right in range(1,len(nums)):
            current = max(nums[right],current + nums[right])
            maximum = max(maximum,current)

        return maximum
        




