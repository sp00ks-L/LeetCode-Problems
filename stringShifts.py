from collections import deque


class Solution:
    def stringShift(self, s, shift):
        sd = deque(s)
        for block in shift:
            if block[0] == 0:  # Left shift
                sd.rotate(-1 * block[1])
            else:
                sd.rotate(block[1])
        out = ''
        for c in sd:
            out += c
        return out




