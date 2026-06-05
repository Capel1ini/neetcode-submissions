class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rec = defaultdict(list)
        for x in nums:
            rec[x].append(x)
        sorted_desc = sorted(rec.items(), key=lambda item: len(item[1]), reverse=True)
        return [item[0] for item in sorted_desc[:k]]
        