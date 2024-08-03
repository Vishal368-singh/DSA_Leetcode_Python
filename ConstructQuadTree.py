# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid):
        def AllCheck(grid, x, y, n):
            val = grid[x][y]
            for i in range(x, x + n):
                for j in range(y, y + n):
                    if grid[i][j] != val:
                        return False
            return True
        
        def solve(grid, x, y, n):
            if n == 1 or AllCheck(grid, x, y, n):
                return Node(grid[x][y], True, None, None, None, None)
            else:
                root = Node(False, False, None, None, None, None)
                half = n // 2
                root.topLeft = solve(grid, x, y, half)
                root.topRight = solve(grid, x, y + half, half)
                root.bottomLeft = solve(grid, x + half, y, half)
                root.bottomRight = solve(grid, x + half, y + half, half)
                return root
        
        return solve(grid, 0, 0, len(grid))

Sol = Solution()

n = int(input("Enter the length of grid: "))
grid = []
for i in range(n):
    grid.append(list(map(int, input().split(','))))
root = Sol.construct(grid)
def printQuadTree(node, indent=""):
    if node is None:
        return
    print(indent + f"Node(val={node.val}, isLeaf={node.isLeaf})")
    if not node.isLeaf:
        print(indent + "Top Left:")
        printQuadTree(node.topLeft, indent + "  ")
        print(indent + "Top Right:")
        printQuadTree(node.topRight, indent + "  ")
        print(indent + "Bottom Left:")
        printQuadTree(node.bottomLeft, indent + "  ")
        print(indent + "Bottom Right:")
        printQuadTree(node.bottomRight, indent + "  ")
printQuadTree(root)
