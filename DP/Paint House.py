"""
Logic : DP 
        At each point we want minimum of cost of red, blue, green
        At any point, total cost of red = cost of red at this house + min(total cost of blue at prev house,
                                                                         total cost of green at prev house)

Time complexity : O(N) -> Each cost is examined only once
Space complexity : O(N) -> We need array of size N to store total cost of all the houses
"""
class Solution(object):
    def paintHouse(self, houses):
        red = [None]*len(houses)
        green = [None]*len(houses)
        blue = [None]*len(houses)
        red[0] = houses[0][0]
        blue[0] = houses[0][1]
        green[0] = houses[0][2]

        #print red, blue, green

        for i in range(1,len(houses)):
            red[i] = min(houses[i][0] + blue[i-1], houses[i][0] + green[i-1])
            blue[i] = min(houses[i][1] + red[i-1], houses[i][1] + green[i-1])
            green[i] = min(houses[i][2] + red[i-1], houses[i][2] + blue[i-1])
            print red, green, blue
        return min(red[-1], green[-1], blue[-1])

print Solution().paintHouse([[17,2,17], [16,16,5], [14,3,19]])

