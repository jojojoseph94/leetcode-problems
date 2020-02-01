"""
Logic : We do a BFS on the flights, starting with the flights from source, adding each flight
        from starting point to other points.
        We check all the flights in the queue, then add the flights from there to the queue.
        We add flights from there if the cost is less than current minimum.
        We keep doing this till we reach K stops

Time Complexity : O(N) -> N being the number of flights. (Worst case is all the flights being checked)
                          BFS complexity is O(N)
Space complexity : BFS O(N)
"""
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        cost = 9999999
        stops = 0
        flights_dict = {}
        queue = []
        for i in range(0,len(flights)):
            if flights[i][0] in flights_dict:
                flights_dict[flights[i][0]].append(flights[i])
            else:
                flights_dict[flights[i][0]] = [flights[i]]
            if src == flights[i][0] and dst == flights[i][1]:
                cost = min(cost, flights[i][2])
                stops = 1
            elif src == flights[i][0]:
                queue.append(flights[i]+[0])
        #one stop
        #explore all other paths
        visited = {}
        while queue:
            #print queue
            flight = queue.pop(0)
            if flight[3] > K:
                break
            if flight[1] == dst:
                cost = min(cost, flight[2])
            # find the outgoing flight
            if flight[1] in flights_dict:
                out_flights = flights_dict[flight[1]]
                for out_flight in out_flights:
                    if out_flight[2] + flight[2] <= cost:
                        # put only till K
                        queue.append([out_flight[0], out_flight[1], out_flight[2] + flight[2]]+[flight[3] + 1])
        if cost == 9999999:
            return -1
        return cost