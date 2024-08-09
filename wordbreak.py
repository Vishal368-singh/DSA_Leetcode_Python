class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False]*(len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[-1]
sol = Solution()
s = input("Enter the string :")
wordDict = input("Enter the word dictionary :").split(',')
print(sol.wordBreak(s, wordDict)) 