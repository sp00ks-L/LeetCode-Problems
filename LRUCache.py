from collections import OrderedDict


class LRUCache:
    '''
    Design and implement an LRUCache with the operations get and put
    '''

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict.fromkeys(range(1, 1 + capacity))  # init size of dict

    def get(self, key):
        # maybe implement get to move to end
        # this makes sure get is thought of as 'using' that element
        if key in self.cache and self.cache[key] is not None:
            self.cache.move_to_end(key, last=True)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        # need to retrieve capacity -> if put is over size then do something
        # just init correct size therefore you always need to pop if its a new key
        if key in self.cache:
            del self.cache[key]
        else:
            self.cache.popitem(last=False)
        self.cache.__setitem__(key, value)
