class Solution:
    def productExceptSelf(self, nums):
        '''
        Given an integer array nums, return an array such that output[i]
        is equal to the product of all elements except nums[i]
        '''
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left[0] = 1
        right[n - 1] = 1

        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]

        for j in reversed(range(n - 1)):
            right[j] = right[j + 1] * nums[j + 1]

        return [a * b for a, b in zip(left, right)]
