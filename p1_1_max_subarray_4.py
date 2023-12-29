import numpy as np
arr1 = [-3.3, 1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -62.2, 34.2, 5.4, -7.8, 1.1, -4.9]
arr2 = [-3.3, 1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]
arr3 = [-3.3, -12.3, -5.5, -1.4, -12.2, -7.8, -4.9]

def algo4(arr):
    # forward calculation
    max_sum = arr[0]
    max_right = 0
    max_left = 0
    sum = arr[0]
    left_start = 0
    for i in range(1, len(arr)):
        sum += arr[i]
        if max_sum < sum:
            max_sum = sum
            max_right = i
            max_left = left_start
        if sum < 0:
            sum = 0
            left_start = i + 1
    return max_sum, max_left, max_right

  
def algo4_1(arr):
    # forward calculation
    max_sum = -100000000
    max_right = -1
    sum = 0
    max = -np.inf
    pos_finded = False
    for i in range(len(arr)):
        if not pos_finded:
            if arr[i] <= 0:
                if max < arr[i]:
                    max = arr[i]
                    max_right = i
                continue
            else:
                pos_finded = True
                max = arr[i]

        sum += arr[i]
        if sum > max_sum:
            max_sum = sum
            max_right = i
    if max <= 0:
        return max, max_right, max_right

    # backward calculation
    max_sum = -100000000
    max_left = -1
    sum = 0
    pos_finded = False
    for i in range(len(arr)-1, -1, -1):
        if not pos_finded:
            if arr[i] <= 0:
                continue
            else:
                pos_finded = True
        sum += arr[i]
        if sum > max_sum:
            max_sum = sum
            max_left = i

    sum = 0
    for i in range(max_left, max_right+1):
        sum += arr[i]

    return sum, max_left, max_right
 
if __name__ == '__main__':
    for arr in [arr1, arr2, arr3]:
        sum, max_left, max_right = algo4(arr)
        print(sum, max_left, max_right)



