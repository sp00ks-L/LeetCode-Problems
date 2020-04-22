class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        Given a string containing only '(', ')' and '*' check whether the string is valid
        '*' can represent either an open or a close bracket
        '''
        if not s:
            return True
        low = hi = 0
        for char in s:
            low += 1 if char == '(' else - 1
            hi += 1 if char != ')' else -1
            if hi < 0:
                break
            low = max(low, 0)

        return low == 0


