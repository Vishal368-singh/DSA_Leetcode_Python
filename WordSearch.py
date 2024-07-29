def exist(board, word):
    def dfs(i,j,k):
        if k == len(word)-1:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False      
        temp = board[i][j]
        board[i][j] = '' # Don't check already checked element
        if dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1):
            return True
        board[i][j]=temp
        return False
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==word[0]:
                if dfs(i, j, 0):
                    return True
    return False


word =  input("Enter the word :")
row= int(input("Enter the number of row in board :"))
board =[]
for _ in range(row):
    li=[]
    for k in input().split(","):
        li.append(k)
    board.append(li)
print("Given Word",word)
print("Given Board",board)
if(exist(board,word)):
    print("Word exist in the board")
else:
    print("Word does not exist in the board")

