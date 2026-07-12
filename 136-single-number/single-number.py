class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        return ans

        # freq = Counter(nums)

        # for val in (nums):
        #     if freq[val] == 1:
        #         return val
            