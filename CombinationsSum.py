def combinationSum(candidates, target):
    output =[]
    def makecombinations(idx , li):
        if sum(li)==target:
            output.append(li[:])
            return
        elif sum(li)>target or idx >= len(candidates):
            return
        li.append(candidates[idx])
        makecombinations(idx , li)
        li.pop()
        makecombinations(idx+1,li)
        return output
    return makecombinations(0,[])

candidates =[int(num) for num in input("Enter the array:").split(",")]
target = int(input("Enter the target for combinations :"))
print("Candidate array :",candidates)
print("Combinations pair for target :",combinationSum(candidates,target))