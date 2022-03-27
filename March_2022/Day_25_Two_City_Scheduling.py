class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        refund = []
        totalcost = 0
        for i in range(n):
            totalcost += costs[i][0]
            refund.append(costs[i][1]-costs[i][0])
        refund.sort()
        for j in range(int(n/2)):
            totalcost += refund[j]
        return totalcost