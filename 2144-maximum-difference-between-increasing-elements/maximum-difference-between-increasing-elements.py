class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = nums[0]
        ans = -1

        for x in nums[1:]:
            if x > small:
                ans = max(ans, x - small)
            else:
                small = x

        return ans