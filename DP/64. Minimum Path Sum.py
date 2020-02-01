"""
Brute force solution : Explore all possible paths using BFS and find the minimum costing path to end
Time Complexity : O(2^N), As number of cells increases, the number of paths to be explored increases
                          exponentially

Space complexity : ??

"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get_neigbours(i,j, cost):
            n = []
            if i+1<len(grid):
                n.append([i+1,j,cost + grid[i+1][j]])
            if j+1<len(grid[0]):
                n.append([i,j+1,cost + grid[i][j+1]])
            return n
        #bfs
        total = None
        queue = [[0,0, grid[0][0]]]
        x = len(grid)-1
        y = len(grid[0])-1
        while queue:
            #print queue
            #check if index is dest
            i, j, cost = queue.pop(0)
            if i==x and y==j:
                if total == None:
                    total = cost
                else:
                    total = min(total, cost)
            else:
                #get left and down neighbours
                neighbours = get_neigbours(i,j,cost)
                if neighbours:
                    queue+=neighbours
        return total

"""
Dynamic programming : Each cell can be reached from its top or left.
                      We minimize that cost
                      Initially we fill the top row and left column with values from
                      grid itself. Then we can apply dynamic programming 

Time complexity : O(M*N)
Space complexity : O(M*N) -> this can be optimized to O(M) by discarding results after one row is processed
                          -> to optimize this to O(1), if you reuse the grid matrix itself
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cost = []
        for i in range(0,len(grid)):
            cost.append([])
            for j in range(0,len(grid[0])):
                cost[i].append(None)
        cost[0][0] = grid[0][0]
        #print cost
        for i in range(1,len(grid)):
            cost[i][0] = cost[i-1][0] + grid[i][0]
        for j in range(1,len(grid[0])):
            cost[0][j] = cost[0][j-1] + grid[0][j]
        #print cost
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                cost[i][j] = grid[i][j] + min(cost[i-1][j], cost[i][j-1])
        return cost[-1][-1]
        