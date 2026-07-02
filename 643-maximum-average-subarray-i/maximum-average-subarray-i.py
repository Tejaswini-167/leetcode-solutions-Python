class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])/k
        maximum = window

        for i in range(k,len(nums)):
            window += nums[i] / k
            window -= nums[i-k] / k 

            maximum = max(window,maximum)

        return maximum
