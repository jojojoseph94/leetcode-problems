"""
Nested weight sum : At each element, check if type is list or not
                    If list add to queue increasing the depth
                    else add to sum with multiplier

Time complexity : O(N) -> N being number of iteger values in list
                          Each integer is visited once

Space complexity : O(N) -> We use queue in which each element can come once

"""
class Solution(object):
    def nested_sum(self, nested_list):
        sum_ = 0
        queue = [[nested_list, 1]]
        while queue:
            element, multiplier = queue.pop(0)
            for i in element:
                if type(i) == type([]):
                    queue.append([i, multiplier+1])
                else:
                    sum_+=(i*multiplier)
        return sum_


s = Solution()
print s.nested_sum([[1,1],2,[1,1]])
print s.nested_sum([1,[4,[6]]])
        




