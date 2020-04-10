class Solution(object):
    def singleNumber(self, nums):
        """
        tasks: Given a non-empty array of integers,
        every element appears twice except for one. Find that single one.
        :type nums: List[int]
        :rtype: int

        Example
        -----------
        nums = [4, 1, 2, 1, 2]
        singleNumber(nums) returns 4
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans



