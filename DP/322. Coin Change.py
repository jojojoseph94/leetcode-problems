"""
Coin change 

Brute force soln - 1 : recursively calculate all combinations of coins possible to reach till target
                  if target, save it. Return minimum value.
                  Time complexity : Exponential
Brute force soln 2 : Till amount, keep calculating how many minimum coins are needed to make the value 
                     iterating from index 0 to len(coins)
                     
DP soln

"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [9999]*(amount+1)
        dp[0] = 0
        for i in range(1, len(dp)):
            min_ =  9999
            for j in range(0,len(coins)):
                #print i, coins[j], min_
                if i - coins[j] >= 0:
                    min_ = min(min_, dp[i-coins[j]] + 1)
            dp[i] = min_
        #print dp
        if dp[amount] < 9999:
            return dp[amount]
        else:
            return -1
            
        