from copy import deepcopy
def gernerateParenthesis(n,left,right,result,res):
    if (n <= left)and(n<=right):
        vp =''.join(res)
        result.append(vp)
        return
    if left < n:
        res.append("(")
        gernerateParenthesis(n,left+1,right,result,res)
        res.pop()
    if right<left:
        res.append(")")
        gernerateParenthesis(n,left,right+1,result,res)
        res.pop()
result=[]
n = int(input("Enter the number"))
gernerateParenthesis(n,0,0,result,[])
print(result)