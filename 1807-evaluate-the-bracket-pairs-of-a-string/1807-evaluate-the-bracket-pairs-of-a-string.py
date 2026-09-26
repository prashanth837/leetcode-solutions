class Solution:
    def evaluate(self, s: str, know: list[list[str]]) -> str:
        map={}
        for i in know:
            map[i[0]]=i[1]
        # if "name" in map.keys():
        #     print(map['name'])
        res=""
        a=[]
        op=float('inf')
        s2=""
        for i in range(len(s)):
            if s[i]=='(':
                op=i
                s2=""
            elif s[i]==')':
                if s2 not in map.keys():
                    res+='?'
                else:
                    res+=map[s2]
                a.append(s2)
                print('----')
                s2=""
                op=float('inf')
            else:
                if i>op:
                    s2+=s[i]
                else:
                    res+=s[i]
            print(s2)

        print(a)
        
            
        return res
                
                