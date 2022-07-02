# Solution 1 - Converting columns to rows and reversing them using zip(*list)
# Time : O(n**2)
# Space : O(1)

class Solution1:
    def rotate(self, matrix: list[list[int]]) -> None:
        tmp = list(map(list,zip(*matrix)))
        for i in range(len(tmp)):
            matrix[i] = tmp[i][::-1]

# Solution 2 - Converting columns to rows and reversing them without using inbuilt functions
# Time : O(n**2)
# Space : O(1)
class Solution2:
    def rotate(self, matrix: list[list[int]]) -> None:
        length = len(matrix)
        for i in range(length):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            left = 0
            right = len(row) - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1


nums = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
testcheck = Solution1()
testcheck.rotate(nums)
print(nums)

