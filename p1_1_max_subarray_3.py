
arr1 = [-3.3, 1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -62.2, 34.2, 5.4, -7.8, 1.1, -4.9]
arr2 = [-3.3, 1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]
arr3 = [-3.3, -12.3, -5.5, -1.4, -12.2, -7.8, -4.9]

# to find the maximum sum of subarray
def algo3(arr, left, right):
    # print(left, right)
    # The illegal case
    if left >= right:
        print('left index should < right index')
        return None
    
    # The simplest case
    if left == right - 1:
        return arr[left], left, right
    
    # Call the function recursively to find the maximum sum of the left subarray
    max_sum1, max_left1, max_right1 = algo3(arr, left, (left+right-1)//2+1)
    max_sum2, max_left2, max_right2 = algo3(arr, (left+right-1)//2+1, right)

    # Calculate the sum between max_left1 and max_right2
    max_left3 = max_left1
    max_right3 = max_right2
    max_sum3 = 0
    for k in range(max_left3, max_right3):
        max_sum3 += arr[k]
    
    # Compare the three results and return the maximum
    if max_sum1 > max_sum2 and max_sum1 > max_sum3:
        return max_sum1, max_left1, max_right1
    if max_sum2 > max_sum1 and max_sum2 > max_sum3:
        return max_sum2, max_left2, max_right2
    if max_sum3 > max_sum1 and max_sum3 > max_sum2:
        return max_sum3, max_left3, max_right3
    


if __name__ == '__main__':
    for arr in [arr1, arr2, arr3]:
        sum, max_left, max_right = algo3(arr, 0, len(arr))
        print(sum, max_left, max_right)