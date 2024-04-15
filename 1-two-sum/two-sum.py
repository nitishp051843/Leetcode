class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_map = {}
        for i in range(len(nums)):
            if nums[i] in ind_map:
                return [i, ind_map[nums[i]]]
            ind_map[target - nums[i]] = i