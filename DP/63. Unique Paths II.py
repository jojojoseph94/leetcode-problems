"""
Logic : Very similar to Unique paths. Fill top row and left row with 1s. 
        But if there are objects in the grid or if the path to previous cell dose not exist
        then set path to zero.
        
        then for each element in grid, num of paths is equal to paths to cell above and cell left to 
        this current cell.
        But if there is an object in the grid, set the paths to zero
Time Complexity : O(M*N)
Space Complexity : O(M*N)
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        paths = []
        for i in range(0,len(obstacleGrid)):
            paths.append([])
            for j in range(0,len(obstacleGrid[0])):
                paths[i].append(None)
        # fill the top and left rows
        paths[0][0] = int(not(obstacleGrid[0][0]))
        for i in range(1,len(obstacleGrid[0])): 
            if obstacleGrid[0][i] == 0 and paths[0][i-1] == 1:
                paths[0][i] = 1
            else:
                paths[0][i] = 0
        for j in range(1,len(obstacleGrid)):
            if obstacleGrid[j][0] == 0 and paths[j-1][0]== 1:
                paths[j][0] = 1
            else:
                paths[j][0] = 0
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    paths[i][j] = paths[i-1][j]+paths[i][j-1]
                else:
                    paths[i][j] = 0
        return paths[-1][-1]