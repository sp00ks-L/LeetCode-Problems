import re


def get_string(string):
    '''
    Uses regex matching to identify patterns including #
    :param string: string
    :return: reformatted string
    '''
    while '#' in string:
        hashtag = re.search('^#', string)
        if hashtag is None:
            pattern = re.search('[a-z]#', string)[0]
            string = string.replace(pattern, '')
        else:
            string = string[1:]

    return string


class Solution:
    def backspaceCompare(self, s, t):
        '''
        Given 2 strings, s and t, return if they are equal when typed into empty text editors
        # means a backspace
        :param s: string 1
        :param t: string 2
        :return: bool
        '''
        return get_string(s) == get_string(t)
