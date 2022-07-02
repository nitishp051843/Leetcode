# Solution 1 - Recursion
# Time : O(n**2)
# Space : O(n)

class Solution1:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        else:
            prev = self.generate(numRows - 1)
            nminus1row = prev[-1]
            curr = []
            for i in range(1,len(nminus1row)):
                curr.append(nminus1row[i-1] + nminus1row[i])
        return prev + [[1] + curr + [1]]

# Solution 1 - Iteration
# Time : O(n**2)
# Space : O(n)

class Solution2:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        else:
            result = [[1],[1,1]]
            for i in range(2,numRows):
                check = result[i-1]
                temp = []
                for j in range(len(check)-1):
                    temp.append(check[j] + check[j+1])
                result.append([1] + temp + [1])
        return result

testcase1 = Solution1()
print(testcase1.generate(5))