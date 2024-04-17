class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1

        hashmap_items_sorted = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in hashmap_items_sorted][:k]

