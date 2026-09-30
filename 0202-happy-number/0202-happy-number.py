class Solution:
    def isHappy(self, n: int) -> bool:
        m=str(n)
        while True:
            su=0
            for i in m:
                su+=int(i)*int(i)
            m=str(su)
            if int(m)==1:
                return True
            if int(m)==4:
                return False

        