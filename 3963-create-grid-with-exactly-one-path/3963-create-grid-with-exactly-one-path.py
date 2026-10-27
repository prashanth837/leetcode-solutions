class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[]
        for i in range(m):
            r=""
            for j in range(n):
                if i==0 or j==n-1:
                    r+='.'
                else:
                    r+='#'
            grid.append(r)
        return grid