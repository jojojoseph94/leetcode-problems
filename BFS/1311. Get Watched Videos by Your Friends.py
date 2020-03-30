"""
Soln : Perform BFS on levels, keeping track of the visited nodes.
       Add a node to level only if it is not visited before
       Then count the movies by the nodes, sort them using count, 
       but if count is same then sort alphabetically.
Time Complexity : BFS O(N) - Worstcase
                   Sorting O(Nlog(N))
                   Combined -> O(Nlog(N))
Space complexity : O(N)
"""
class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        def find_level_friend(lvl, ids, visited):
            if lvl == 0:
                return list(ids)
            ids_next_level = set()
            for i in ids:
                for j in friends[i]:
                    if j not in visited:
                        ids_next_level.add(j)
                        visited.add(j)
            return find_level_friend(lvl-1, list(ids_next_level), visited)
        
        friends_at_level = find_level_friend(level, [id], set([id]))
        counts = collections.Counter([vd for i in friends_at_level for vd in watchedVideos[i]])
        return [count[1] for count in sorted([(counts[vd], vd) for vd in sorted(counts.keys())])]
        
            
            
        