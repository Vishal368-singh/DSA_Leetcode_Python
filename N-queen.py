# i+j==qx[k]+qy[k]:
#  checks if the current position is on the same diagonal 
# (from top-left to bottom-right) as the queen.
# i-j==qx[k]-qy[k]: 
# checks if the current position is on the same diagonal
#  (from top-right to bottom-left) as the queen.
from copy import deepcopy

res, qx, qy = [], [], []

def is_safe(row, col, qx, qy, n):
    if row >= n or col >= n:
        return False
    if row in qx:
        return False
    if col in qy:
        return False
    for k in range(len(qx)):
        if row + col == qx[k] + qy[k] or row - col == qx[k] - qy[k]: #To check the current position
            return False
    return True

def n_queen(row, n, qx, qy, nq):
    if row == n:
        res.append(deepcopy(nq))
        return
    for col in range(n):
        if is_safe(row, col, qx, qy, n):
            qx.append(row)
            qy.append(col)
            nq[row][col] = 'Q'
            n_queen(row + 1, n, qx, qy, nq)
            qx.pop()
            qy.pop()
            nq[row][col] = '.'
    return

n = int(input("Enter the number of queens: "))
nq = [['.'] * n for _ in range(n)]
n_queen(0, n, qx, qy, nq)

for i, solution in enumerate(res):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(' '.join(row))
    print()