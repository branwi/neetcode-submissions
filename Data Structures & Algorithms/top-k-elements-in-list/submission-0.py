from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []
        l = []
        for num in nums:
            count[num] += 1
        
        for n, c in count.items():
            heapq.heappush(heap, (-c, n))
        
        for i in range(k):
            l.append(heapq.heappop(heap)[1])
        
        return l