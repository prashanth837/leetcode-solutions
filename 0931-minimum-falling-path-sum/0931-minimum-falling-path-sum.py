class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[float('inf') for i in range(m+2)] for i in range(n)]
        dp[0]=[float(inf)]+matrix[0]+[float(inf)]
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])-1):
                print(i,j)
                dp[i][j]=min((matrix[i][j-1]+dp[i-1][j-1]),(matrix[i][j-1]+dp[i-1][j]),(matrix[i][j-1]+dp[i-1][j+1]))
        return min(dp[-1])