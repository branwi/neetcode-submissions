import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        heapq.heapify_max(stones)
        heap = stones
        while len(heap) > 1:
            x = heapq.heappop_max(heap)
            y = heapq.heappop_max(heap)
            if x != y:
                heapq.heappush_max(heap, max(y-x, x-y))
        if heap:
            return heap[0]
        else:
            return 0