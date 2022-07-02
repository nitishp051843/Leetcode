class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1],reverse=True)
        result = 0
        for numofboxes, unitsperbox in boxTypes:
            minboxes = min(numofboxes,truckSize)
            result += minboxes * unitsperbox
            truckSize -= minboxes
        return result

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
testcase = Solution()
print(testcase.maximumUnits(boxTypes,truckSize))