class Solution:
    def uniquePathsWithObstacles(self, ob: list[list[int]]) -> int:
        m=len(ob)
        n=len(ob[0])
        dp=[[0 for i in range(n+2)] for j in range(m)]
        print(dp)
        obs=False
        for i in range(0,1):
            for j in range(1,len(dp[0])-1):
                if ob[i][j-1]==1:
                    dp[i][j]=0
                    obs=True
                elif obs:
                    dp[i][j]=0
                else:
                    dp[i][j]=1
        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])-1):
                if ob[i][j-1]==1:
                    dp[i][j]='x'
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])-1):
                if dp[i][j]=='x':
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[-1][-2]