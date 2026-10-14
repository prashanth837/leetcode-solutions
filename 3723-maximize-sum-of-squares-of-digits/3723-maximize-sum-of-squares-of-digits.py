class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum<10:
            return str(sum)+"0"*(num-1)
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
        if len(ans)==num:
            return ans
        m=num-len(ans)
        ans=ans+'0'*m
        return ans
