class Solution:
    def rangeBitwiseAnd(self, m, n):
        '''
        Given a range [m, n] where 0 <= m <= n <= 2147483647
        return the bitwise and of all numbers inclusive
        '''
        while m < n:
            n -= (n & -n)

        return n

