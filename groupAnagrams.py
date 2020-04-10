from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        """
        From an array of strings, if the string is an anagram, group it with equivalent strings
        :param strs: List[string]           ["eat", "tea", "tan", "ate", "nat", "bat"]
        :return: List[List[string]]         [["ate","eat","tea"],
                                            ["nat","tan"],
                                            ["bat"]]
        """
        grouped_words = defaultdict(list)

        for s in strs:
            grouped_words[''.join(sorted(s))].append(s)

        return [val for val in grouped_words.values()]


def groupAnagrams2(strs):
    """
    Same algorithm but without defaultdict
    :param strs: List[string]
    :return: :List[List[string]]
    """
    grouped_words = dict()

    for s in strs:
        key = "".join(tuple(sorted(s)))
        if key in grouped_words:
            grouped_words[key] = grouped_words.get(key) + " " + s
        else:
            grouped_words.update({key: s})

    return [group.split(' ') for group in grouped_words.values()]
