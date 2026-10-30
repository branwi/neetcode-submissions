import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify_max(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        heap = self.heap.copy()
        for i in range(self.k - 1):
            heapq.heappop_max(heap)
        return heap[0]
