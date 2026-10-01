class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        ist=True
        for i in s:
            if i=='[' or i=='{' or i=='(':
                a.append(i)
            if i==']':
                if len(a)==0 or a[-1]!='[':
                    return False
                a.pop()   
            elif i=='}':
                if len(a)==0 or a[-1]!='{':
                    return False
                a.pop()
            elif i==')':
                if len(a)==0 or a[-1]!='(':
                    return False
                a.pop()
        if len(a)==0:
            return True
        else:
            return False
       
        
        