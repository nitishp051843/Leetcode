# Solution 1 - Bubble Sort
# Time : O(n**2)
# Space : O(1)


class Solution1:
    def sortColors(self, nums: list[int]) -> None:
        ''' For sorting elements in ascending order'''
        for i in range(len(nums)):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

# Solution 2 - Selection Sort
# Time : O(n**2)
# Space : O(1)

class Solution2:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums)):
            curr_min = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[curr_min]:
                    curr_min = j
            nums[i],nums[curr_min] = nums[curr_min], nums[i]

# Solution 4 - Counting Sort
# Time : O(n)
# Space : O(n)

class Solution4:
    def sortColors(self, nums: list[int]) -> None:
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1

        ind = 0
        for i in range(3):
            if i in counts:
                tmp = counts[i]
                nums[ind:ind + tmp] = [i] * tmp
                ind += tmp

# Testcase

testcase1 = Solution1()
nums = [4,2,7,45,2,8,3,13,4,2]
testcase1.sortColors(nums)
print(nums)
