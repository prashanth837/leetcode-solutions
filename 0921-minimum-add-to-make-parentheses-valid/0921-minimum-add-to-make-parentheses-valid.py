class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[0]
        for i in s:
            if i=='(':
                stack.append(i)
            elif i==')':
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)-1