# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def point(self, matrix):
        '''
        This was an interactive problem - use the binaryMatrix interface to retrieve necessary info

        Task: Find the the leftmost column that contained a one
        Constraint - only 1000 calls to binaryMatrix.get(x, y) allowed
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        ind = 10000
        back_ele = cols - 1

        rows, cols = binaryMatrix.dimensions()
        ind = 10000
        back_ele = cols - 1
        for row in range(rows):
            p = binaryMatrix.get(row, back_ele)
            if not p:
                continue
            while p:
                ind = min(ind, back_ele)
                if back_ele - 1 < 0:
                    break

                back_ele -= 1
                p = binaryMatrix.get(row, back_ele)

        if ind > 100:
            return -1
        else:
            return ind
