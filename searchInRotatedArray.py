class Solution:
    def search(self, nums, target):
        '''
        Quick pythonic way to find a target in a rotated array
        '''
        try:
            ind = nums.index(target)
            return ind
        except ValueError:
            return -1

    def binSearch(self, nums, target):
        '''
        Uses binary search to complete same task.
        - First finds middle and checks if it is the target
        - Compares whether middle is greater than first value
            - Repeat this for target (this gives incite into array rotation)
        - Move binary search accordingly
        '''
        n = len(nums)
        if n == 0:
            return - 1
        low = 0
        high = n - 1
        first = nums[0]
        while low <= high:
            mid = low + (high - low) // 2
            value = nums[mid]
            if value == target:
                return mid

            am_big = value >= first
            target_big = target >= first
            if am_big == target_big:
                if value < target:
                    low = mid + 1
                else:
                    high = mid - 1

            else:
                if am_big:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

