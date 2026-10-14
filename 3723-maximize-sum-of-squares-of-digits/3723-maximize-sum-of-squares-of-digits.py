class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9<sum:
            return ""
        ans=""
        while sum:
            if sum>9:
                ans+='9'
                sum-=9
            else:
                ans+=str(sum)
                sum-=sum
        x=len(ans)
        m=num-x
        ans=ans+'0'*m
        return ans
