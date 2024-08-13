class Solution:
    def triangle(self, triangle):
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]

sol = Solution()
triangle = []
row = int(input("Enter the number of rows: "))
for _ in range(row):
    triangle.append([int(j) for j in input("Enter the elements for row {}: ".format(_+1)).split(",")])

print("Minimum path sum from top to bottom:", sol.triangle(triangle))