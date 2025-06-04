class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        current_gas = 0
        start = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += (gas[i] - cost[i])
            if current_gas < 0:
                start = i+1
                current_gas = 0
        if total_gas < total_cost:
            return -1
        return start


'''
gas =
[1,2,3,4,5]
cost =
[3,4,5,1,2]
3

gas =
[2,3,4]
cost =
[3,4,3]
-1


'''