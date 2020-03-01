def make_change(coins, amount):
    dp = [float('inf')]*(amount+1)
    dp[0] = 0
    for coin in coins:
        for c in range(coin,amount+1):
            dp[c] = min(dp[c], dp[c-coin]+1)
    return dp[amount] if dp[amount]!=float('inf') else -1

print(make_change([1,2,3,4,5,6,7], 25))


