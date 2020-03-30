"""
Logic: DP -> make a paths grid
             fill top row and left row with 1s
             The number of paths to a cell is equal to sum of
             number of paths in cell just above and cell to the left

Time complexity : O(M*N)
Space complexity : O(M*N) -> Optimization process row by row and keep last row only
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = []
        for i in range(0,n):
            paths.append([])
            for j in range(0,m):
                paths[i].append(None)
        # fill the top and left rows
        for i in range(0,m):
            paths[0][i] = 1
        for j in range(0,n):
            paths[j][0] = 1
            
        for i in range(1,n):
            for j in range(1,m):
                paths[i][j] = paths[i-1][j]+paths[i][j-1]
        return paths[-1][-1]