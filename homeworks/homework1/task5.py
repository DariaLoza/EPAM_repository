""""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""


def find_maximal_subarray_sum(nums, k):
    """This function returns the sum of sub-array with length less equal to k"""
    sum_list = []
    for sub_arr_len in range(1, k + 1):
        for start_position in range(len(nums) - sub_arr_len + 1):
            sum_list.append(sum(nums[start_position : start_position + sub_arr_len]))
    return max(sum_list)
