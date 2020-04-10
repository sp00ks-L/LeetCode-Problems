class Solution:

    def countElements(self, arr):
        """
        Given an array of ints, count element x such that x + 1 is also in the array
        If there are duplicates, count them separately
        :param arr: List[int]           [1, 3, 2, 3, 5, 0]
        :return: int                    3
        """
        count = 0
        for i in range(len(arr)):
            if arr[i] + 1 in arr:
                count += 1

        return count
