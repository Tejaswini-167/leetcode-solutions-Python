class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        small = nums[0]
        ans = -1

        for i in nums[1:]:
            if i > small:
                ans = max(ans ,i - small)
            small = min(i,small)
        return ans
            
        