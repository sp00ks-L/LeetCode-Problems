class Solution:
    def max_sub_array(self, nums):
        """
        Divide and Conquer
        ------------------
        - Uses recursion to break down array into smaller chunks before combining the result into a max() function

        :param nums: List[int]
        :return: List[int] such that it is has the maximum sum of a sub array
        """
        n = len(nums)

        def get_cross_sum(arr, low, mid, high):
            left_sum = -1e8
            total = 0

            for i in range(mid, low - 1, -1):
                total += arr[i]
            if total > left_sum:
                left_sum = total

            right_sum = -1e8
            total = 0

            for i in range(mid + 1, high + 1):
                total += arr[i]
            if total > right_sum:
                right_sum = total

            return left_sum + right_sum

        def max_sub_array(arr, low, high):
            # base case
            if high == low:
                return arr[low]

            mid = (low + high) // 2

            return max(max_sub_array(arr, low, mid),
                       max_sub_array(arr, mid + 1, high),
                       get_cross_sum(arr, low, mid, high))

        return max_sub_array(nums, 0, n - 1)


def kadanes(nums):
    """
    Most effective solution to this problem
    Slight implementation differences depending on the problem.
    - If you want to return 0 for an array of negative values [-2, -1 -4, -8] then
            current_sum = max(0, current_sum + num)
    - If you want to return the true maximum from [-2, -1, -4, -8] which returns -1 then
            current_sum = max(num, current_sum + num)


    :param nums: List[int]
    :return: List[int] such that it is has the maximum sum of a sub array
    """
    best_sum = -1e8
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        best_sum = max(best_sum, current_sum)
    return best_sum
