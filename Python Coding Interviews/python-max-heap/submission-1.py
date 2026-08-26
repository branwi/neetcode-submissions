import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    reverse_heap = []
    l = []
    for n in nums:
        heapq.heappush(reverse_heap, -n)

    while reverse_heap:
        l.append(-heapq.heappop(reverse_heap))

    return l




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
