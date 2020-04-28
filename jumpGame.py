class BackTracking:

    def canJump(self, pos, nums):
        '''
        Where each int in nums[] is the maximum jump length
        is it possible to reach the last index
        '''
        n = len(nums)
        if pos == n - 1:
            return True

        farthestJump = min(pos + nums[pos], n - 1)
        for i in range(farthestJump, pos, -1):
            if self.canJump(i, nums):
                return True

        return False

    def jumpGame(self, nums):
        return self.canJump(0, nums)
