class Solution(object):
    def twoSum(self, nums, target):
        dict = {}

        for index, val in enumerate(nums):
            ans = target - val
            if ans in dict:
                return dict[ans], index
            dict[val] = index
      