def findMaxLength(nums):
    '''
    if we use a running total; if 1 add 1 if 0 - 1
    identify longest array with sum 0
    :param nums:
    :return:
    '''
    count = 0
    d = {0: 0}
    maxlen = 0
    for i, v in enumerate(nums):
        count += 2 * v - 1
        if count in d:
            maxlen = max(maxlen, i + 1-d[count])
        else:
            d[count] = i + 1

    return maxlen
