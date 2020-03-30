"""
Problem : Check neighbour of each rotten node and if its fresh, make it rotten and add it to queue
          Do BFS, keeping track of indexes and minutes passed
Time Complexity : O(M*N)
Space Complexity : O(M*N)
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get_fresh_neighbours(i,j, minute):
            neigh = []
            if (i+1 < len(grid) and grid[i+1][j] == 1):
                grid[i+1][j] = 2
                neigh.append([i+1,j, minute+1])
            if (i-1 >=0 and grid[i-1][j] == 1):
                grid[i-1][j] = 2
                neigh.append([i-1,j, minute+1])
            if (j+1 < len(grid[i]) and grid[i][j+1] == 1):
                grid[i][j+1] = 2
                neigh.append([i,j+1, minute+1])
            if (j-1 >=0 and grid[i][j-1] == 1):
                grid[i][j-1] = 2
                neigh.append([i,j-1, minute+1])
            return neigh
        ans = 0
        queue = []
        visited = {}
        flag = True
        # find first rotten orange
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i,j, 0])
                elif grid[i][j] == 1:
                    flag = False
                    #visited[[i,j]] = True
        if flag:
            return 0
        while queue:
            #print queue
            i,j, minute = queue.pop(0)
            ans = minute
            #check neighbours
            neighbours = get_fresh_neighbours(i,j, minute)
            if neighbours:
                #print "At minute ", minute, " rotting neighbours ", i, j, neighbours
                queue+=neighbours
        #check for fresh orange
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        return ans
                
            