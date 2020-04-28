from collections import Counter


class FirstUnique:
    '''
    Implement a FirstUnique class that will allow you to
    retrieve the first unique integer in the queue
    '''

    def __init__(self, nums):
        self.q = Counter(nums)

    def showFirstUnique(self) -> int:
        for item in self.q.items():
            if item[1] == 1:
                return item[0]
            else:
                continue
        return -1

    def add(self, value: int) -> None:
        if value in self.q:
            self.q[value] += 1
        else:
            self.q.update({value: 1})

