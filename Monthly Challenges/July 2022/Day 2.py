class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]) -> int:
        # Adding final and intial cuts to the cake
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]

        horizontalBlocks = []
        verticalBlocks = []
        # Diff elements
        for i in range(len(horizontalCuts) - 1):
            horizontalBlocks.append(horizontalCuts[i + 1] - horizontalCuts[i])

        for i in range(len(verticalCuts) - 1):
            verticalBlocks.append(verticalCuts[i + 1] - verticalCuts[i])

        return max(horizontalBlocks) * max(verticalBlocks) % (10 ** 9 + 7)


testcase = Solution()
print(testcase.maxArea(5, 4, [1, 3], [1]))
