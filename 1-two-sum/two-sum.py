class Solution(object):
    def twoSum(self, nums, target):
   
        d = {}
        for i, val in enumerate(nums):
            x = target - val

            if x in d:
                return d[x],i
            d[val] = i