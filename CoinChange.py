class Solution:
    def coinChange(self, coins, amount) :
        if amount ==0:
            return 0
        dp = [float('inf')]*(amount+1)
        dp[0]=0
        for coin in coins:
            for x in range(coin,amount+1):
                dp[x]=min(dp[x],dp[x-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
sol = Solution()
amount = int(input("Enter the amount :"))
coins = list(map(int, input("Enter the coins :").split(",")))
print("Minimum coin required:",sol.coinChange(coins, amount))