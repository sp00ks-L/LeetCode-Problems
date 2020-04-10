class Solution:
    def move_zeros(self, nums):
        """
        Takes an array of ints and moves zeroes
        to the end of the array while maintaining the order of the remaining ints
        :param nums: List[int]      [0, 1, 0, 3, 12]
        :return: List[int]          [1, 3, 12, 0, 0]
        """
        n = len(nums)
        nxt = 0
        for num in nums:
            if num != 0:
                nums[nxt] = num
                nxt += 1
        for i in range(nxt, n):
            nums[i] = 0

        return nums
