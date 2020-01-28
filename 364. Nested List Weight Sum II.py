"""
Nested weight sum II : Add the numbers to stack keeping track of depth
                       Process stack from bottom with each element multiplied by depth
                       When a level changes, decrease the depth

Time complexity : O(N) -> Each node visited eactly once -> 2 pass
Space complexity : O(N) -> one stack and one queue

"""
class Solution(object):
    def nested_sum(self, nested_list):
        sum_ = 0
        stack2=[]
        depth = 1
        queue = [[nested_list, 1]]
        while queue:
            node,level = queue.pop(0)
            this_level = True
            for i in node:
                if type(i) == type([]):
                    queue.append([i, level+1 ])
                    if this_level:
                        depth+=1
                        this_level = False
                else:
                    stack2.append([i, level])
        prev_level = None
        while stack2:
            ele, level = stack2.pop(0)
            #print ele, level, sum_
            if prev_level == None:
                prev_level = level
            if level!= prev_level:
                depth-=1
            print "Sum equals ", ele, " * " , depth
            sum_+=  (ele * depth)
            prev_level = level
        return sum_

s = Solution()
print s.nested_sum([[1,1],2,[1,1]])
print s.nested_sum([1,[4,[6]]])
        




