from heapq import heapify, heappop, heappush, nlargest


def lastStone(heap):
    """
    You have a collection of stones with positive integer weights
    - Choose the 2 heaviest and smash them together where x <= y
    - If x == y, both stones are destroyed
    - If x != y, stone x is destroyed and weight of y is y-x
    - There is at most 1 stone left, return the weight if that stone (or of no stones)

    First time using heaps
    :param heap: List[int] that is converted into heap          [2,7,4,1,8,1]
    :return: int (the weight of the remaining stone)            returns 1
    """
    heapify(heap)
    while len(heap) > 1:
        twoLargest = nlargest(2, heap)
        heappush(heap, abs(twoLargest[0] - twoLargest[1]))
        for num in twoLargest:
            heap.remove(num)
    return heap[0]


def lstone(heap):
    """
    Leverages heappop removing smallest element by converting all ints to negative
    :param heap: List[int]
    :return: int
    """
    new_list = [-x for x in heap]
    heapify(new_list)
    while len(new_list) > 1:
        y = heappop(new_list)
        x = heappop(new_list)
        if y != x:
            heappush(new_list, y - x)
    if len(new_list):
        return -heappop(new_list)
    return 0
