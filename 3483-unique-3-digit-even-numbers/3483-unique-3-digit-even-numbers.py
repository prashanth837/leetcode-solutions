class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        a=[]
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i!=j and j!=k and k!=i:
                        x=digits[i]*100+digits[k]*10+digits[j]
                        if x%2==0 and len(str(x))==3:
                            if x not in a:
                                a.append(x)
                                print(a)
        return len(a)