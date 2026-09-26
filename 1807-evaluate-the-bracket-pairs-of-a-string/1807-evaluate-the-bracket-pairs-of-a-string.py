class Solution:
    def evaluate(self, s: str, know: list[list[str]]) -> str:
        map={}
        for i in know:
            map[i[0]]=i[1]
        # if "name" in map.keys():
        #     print(map['name'])
        res=""
        op=float('inf')
        s2=""
        for i in range(len(s)):
            if s[i]=='(':
                op=i
                s2=""
            elif s[i]==')':
                if s2 in map.keys():
                    res+=map[s2]
                else:
                    res+="?"
                s2=""
                op=float('inf')
            else:
                if i>op:
                    s2+=s[i]
                else:
                    res+=s[i]
        return res
                
                