
arr = [1.5, -12.3, 3.2, -5.5, 23.2, 3.2, -1.4, -12.2, 34.2, 5.4, -7.8, 1.1, -4.9]

def algo2(arr):
    max_sum = 0
    max_left = -1
    max_right = -1
    for left in range(len(arr)):
        sum = 0
        for right in range(left, len(arr)):
            sum += arr[right]

            if sum > max_sum:
                max_sum = sum
                max_left = left
                max_right = right

    print(max_sum, max_left, max_right)
    return max_sum, max_left, max_right


if __name__ == '__main__':
    algo2(arr)


