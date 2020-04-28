"""
Solution: DP formula 
          if character at indexes match, dp[i+1][j+1] = dp[i][j]+1
          else dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

          Why i+1 and j+1? We initialize all indexes with zero and entry in 
          dp[i][j] corresponds to the solution when text1 is i length and text2 is j length
          We need to cover 0 length case too.
"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        dp = []
        for i in range(0,len(text1)+1):
            dp.append([0]*(len(text2)+1))
        #print dp
        for i in range(0,len(text1)):
            for j in range(0,len(text2)):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
            #print dp
        return dp[-1][-1]
        