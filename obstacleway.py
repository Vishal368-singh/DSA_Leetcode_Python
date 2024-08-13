class solutions:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0]==0:
                dp[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j]==0:
                dp[0][j] = 1
            else:
                break
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

sol = solutions()
obstacleGrid= []
row= int(input("Enter the number of row:"))
for i in range(row):
    li=[]
    for j in input("Enter the element:").split(","):
        li.append(int(j))
    obstacleGrid.append(li)
print("Number of unique path with obstacles are :", sol.uniquePathsWithObstacles(obstacleGrid))