"""
Problem : BFS only
Time complexity : We need to visit all children. Worst case
                  O(N^2)
Space complexity : O(N^2)
Optimization below
"""

"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id_):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        ans = 0
        #bfs
        queue = []
        for e in employees:
            if e.id == id_:
                queue = [e]
                break
        while queue:
            emp = queue.pop(0)
            ans+=emp.importance
            for s in emp.subordinates:
                for e in employees:
                    if e.id == s:
                        queue.append(e)
                        break
        return ans

"""
Optimization -> Use a hashmap to access object in O(1)
This brings down the time complexity to O(N)
"""
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id_):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        ans = 0
        #bfs
        queue = []
        dict_ = {}
        for e in employees:
            if e.id == id_:
                queue = [e]
            dict_[e.id] = e
        while queue:
            emp = queue.pop(0)
            ans+=emp.importance
            for s in emp.subordinates:
                e = dict_[s]
                queue.append(e)
        return ans