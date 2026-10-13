class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1 + nums2)

        n = len(arr)
        mid = n // 2

        if n % 2 == 1:
            return float(arr[mid])
        else:
            return (arr[mid - 1] + arr[mid]) / 2