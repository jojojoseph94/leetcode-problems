"""
Floodfill - BFS version.
Timecomplexity : O(MxN)
Space complexity : O(MxN)

"""
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def check_neighbours(ele, old_color, new_Color):
            x = ele[0]
            y = ele[1]
            neighbours = []
            if x+1 <len(image) and image[x+1][y] == old_color and image[x+1][y] != new_Color:
                neighbours.append([x+1,y])
            if x-1 >-1 and image[x-1][y] == old_color and image[x-1][y] != new_Color:
                neighbours.append([x-1,y])
            if y+1 <len(image[0]) and image[x][y+1] == old_color and image[x][y+1] != new_Color:
                neighbours.append([x,y+1])
            if y-1 >-1 and image[x][y-1] == old_color and image[x][y-1] != new_Color:
                neighbours.append([x,y-1])
            return neighbours
        queue = []
        old_color = image[sr][sc]
        queue.append([sr,sc])
        while queue:
            #print queue
            ele = queue.pop(0)
            image[ele[0]][ele[1]] = newColor
            if check_neighbours(ele, old_color, newColor):
                queue+=check_neighbours(ele, old_color, newColor)
        return image