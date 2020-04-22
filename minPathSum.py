class Solution:
    MAXINT = 100000

    def minPathSum(self, grid):
        '''
        Given a grid of non-negative numbers, find a path from top left to bottom right
        which minimises the sum along the path.
        You can only move down or right
        '''
        # can only go down and right
        # last move is not important so
        # dp[row][col] = current sum
        # greedy doesnt work
        m = len(grid)
        n = len(grid[0])
        dp = [0] + [self.MAXINT] * (n - 1)
        for i in range(m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]

        return dp[-1]
