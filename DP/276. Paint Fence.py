class Solution(object):
    def paintFence(self, n, k):
        """
        n : number of fences
        k : number of colors
        """
        dp = [None]*(n)
        # for first fence
        same = k
        diff = k*(k-1)
        dp[0] = 0
        dp[1] = same + diff
        for i in range(2, n):
            same = diff
            diff = dp[i-1]*(k-1)
            dp[i] = same + diff
        return dp[-1]

print Solution().paintFence(3,2)
print Solution().paintFence(2,4)