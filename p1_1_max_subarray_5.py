import numpy as np
arr1 = [-3.3, 1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -62.2, 34.2, 5.4, -7.8, 1.1, -4.9]
arr2 = [-3.3, 1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]
arr3 = [-3.3, -12.3, -5.5, -1.4, -12.2, -7.8, -4.9]

def algo5(arr):
    n = len(arr)
    min_sum = arr[0]
    sum = arr[0]
    max_sum = arr[0]
    left_idx = 0
    right_idx = 0
    for k in range(n):
        sum += arr[k]
        # max_sum = max(max_sum, sum - min_sum)
        # min_sum = min(min_sum, sum)
        tmp = sum - min_sum
        if max_sum < tmp:
            max_sum = tmp
            right_idx = k
        if min_sum > sum:
            min_sum = sum
            left_idx = k + 1
    return max_sum, left_idx, right_idx

if __name__ == '__main__':
    for arr in [arr1, arr2, arr3]:
        sum = algo5(arr)
        print(sum)
        # print(sum, max_left, max_right)



