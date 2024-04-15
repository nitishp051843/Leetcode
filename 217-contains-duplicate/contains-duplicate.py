class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_count = {}
        for i in nums:
            nums_count[i] = nums_count.get(i, 0) + 1
            if nums_count[i] > 1:
                return True
        return False