class Solution:
    def maxPoints(self, points):
        if len(points)<=2:
            return len(points)
        maxi =1
        for idx,point1 in enumerate(points):
            slopeM = defaultdict(int)
            for j, point2 in enumerate(points[idx+1:]):
                slope = self.slope(point1,point2)
                slopeM[slope]+=1
                maxi = max(slopeM[slope], maxi)
        return maxi+1

    def slope(self, point1 ,point2):
        x1,y1 = point1
        x2,y2 = point2
        if x1-x2==0:
            return
        return (y2-y1)/(x2-x1)
    
sol = Solution()
points=[]
row= int(input("Enter the number of row in point :"))
for _ in range(row):
    li=[]
    for k in input("Enter the row :").split(","):
        li.append(int(k))
    points.append(li)
print("The points are :", points)
print("Maximum points on a line :",sol.maxPoints(points))