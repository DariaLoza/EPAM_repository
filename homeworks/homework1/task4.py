"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """This function computes how many tuples there are such that A[i] + B[j] + C[k] + D[l] is zero """
    dic = {}
    count = 0
    len_list = len(a)

    for i in range(len_list):
        for j in range(len_list):
            sum_element = a[i] + b[j]
            if sum_element in dic:
                dic[sum_element] += 1
            else:
                dic[sum_element] = 1

    for k in range(len_list):
        for i in range(len_list):
            sum_element = c[k] + d[i]
            if -sum_element in dic:
                count += dic.get(-sum_element)

    return count
