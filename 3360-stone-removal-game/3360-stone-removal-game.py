class Solution:
    def canAliceWin(self, n: int) -> bool:
        ali=1
        k=10
        while n>=k:
            n-=k
            k-=1
            ali+=1
            print(n)
        return ali%2==0