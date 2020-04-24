from collections import Counter


class Solution:
    def subarraySum(self, nums, k):
        '''
        Given an int array and an int k, find the total number of
        continuous sub arrays whose sum == k
        '''
        count = Counter()
        count[0] = 1
        ans = cSum = 0
        for num in nums:
            cSum += num
            ans += count[cSum - k]
            count[cSum] += 1
        return ans
