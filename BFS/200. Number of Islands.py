"""
BFS solution. Visit all nodes once. If set to 1, increment count once, add node to queue and set to zero.
While queue, check neighbours, if yes add node to queue and set to zero.
Time Complexity : O(MxN) - Each node gets visited and checked only once.
Space complexity : O(MxN) - At max all nodes can end up in the queue.
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def check_neighbours(k,l):
            #print k,l
            neighbours = []
            if k+1 < len(grid) and grid[k+1][l] == "1":
                neighbours.append([k+1,l])
            if l+1 < len(grid[0]) and grid[k][l+1] == "1":
                neighbours.append([k,l+1])
            if k-1 >= 0 and grid[k-1][l] == "1":
                neighbours.append([k-1,l])
            if l-1 >= 0 and grid[k][l-1] == "1":
                neighbours.append([k,l-1])
            return neighbours
        def set_to_zero(arr):
            for indexes in arr:
                #print indexes, " Arr ", arr
                k = indexes[0]
                l = indexes[1]
                grid[k][l] = "0"
        count = 0
        queue = []
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == "1":
                    queue.append([i,j])
                    set_to_zero([[i,j]])
                    count+=1
                    #print " Entering queue"
                    while queue:
                        #print queue
                        indexes = queue.pop(0)
                        k = indexes[0]
                        l = indexes[1]
                        if check_neighbours(k,l):
                            queue+=check_neighbours(k,l)
                            set_to_zero(check_neighbours(k,l))
        #print count
        return count
                
"""
DFS Solution : Use a stack instead of queue. 
               Visit each node and check if "1", if yes set to zero and add to stack.
               While stack, check if neighbours are "1", if yes add it to stack and set to zero.
Time complexity : O(MxN)
Space complexity : O(MxN)
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def check_neighbours(k,l):
            #print k,l
            neighbours = []
            if k+1 < len(grid) and grid[k+1][l] == "1":
                neighbours.append([k+1,l])
            if l+1 < len(grid[0]) and grid[k][l+1] == "1":
                neighbours.append([k,l+1])
            if k-1 >= 0 and grid[k-1][l] == "1":
                neighbours.append([k-1,l])
            if l-1 >= 0 and grid[k][l-1] == "1":
                neighbours.append([k,l-1])
            return neighbours
        def set_to_zero(arr):
            for indexes in arr:
                #print indexes, " Arr ", arr
                k = indexes[0]
                l = indexes[1]
                grid[k][l] = "0"
        count = 0
        stack = []
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == "1":
                    stack.append([i,j])
                    set_to_zero([[i,j]])
                    count+=1
                    while stack:
                        indexes = stack.pop(-1)
                        k = indexes[0]
                        l = indexes[1]
                        if check_neighbours(k,l):
                            stack+=check_neighbours(k,l)
                            set_to_zero(check_neighbours(k,l))
        return count
                
                    