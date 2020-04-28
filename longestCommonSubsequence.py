class LongestCommonSubsequence:

    def longestString(self, t1, t2):
        '''
        Uses actual string in dp therefore to return answer
        you must use len(dp)
        '''
        dp = [["" for x in range(len(t2))] for y in range(len(t1))]

        for i in range(len(t1)):
            for j in range(len(t2)):
                if t1[i] == t2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = t1[i]
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + t1[i]

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)

        return len(dp[-1][-1])

    def stringLength(self, s1, s2):
        '''
        Uses the length of the string in dp therefore
        no need for len(dp)
        '''
        n = len(s1)
        m = len(s2)

        dp = [[0 for x in range(m)] for y in range(n)]

        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
