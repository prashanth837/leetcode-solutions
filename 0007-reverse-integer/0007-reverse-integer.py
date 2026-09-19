class Solution:
    def reverse(self, x: int) -> int:
        negetive=False
        if x<0:
            negetive=True
            x=x*-1
        str1=str(x)
        str2=str1[::-1]
        num=int(str2)
        if num<-2**31 or num>2**31:
            return 0
        if negetive==True:
            return num*-1
        else:
            return num
        
        