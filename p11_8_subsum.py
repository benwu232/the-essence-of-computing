

def subsum(arr, n):
    sum_dict = {}
    sum = 0
    cnt = 0
    for k, e in enumerate(arr):
        sum += e
        if not sum_dict.get(sum):
            sum_dict[sum] = [k, 1]
        else:
            sum_dict[sum] = [k, sum_dict[sum][1] + 1]
    
    for sum in sum_dict:
        if sum_dict.get(sum-n):
            cnt += sum_dict[sum][1]
    if sum_dict.get(n):
        cnt += sum_dict[n][1]
        
    return cnt


def subsum2(arr, n):
    left = 0
    right = -1
    cnt = 0

    sum = 0
    while right < len(arr) - 1:
        if sum == n:
            cnt += 1
            print(left, right)
            right += 1
            sum += arr[right]
        elif sum < n:
            right += 1
            sum += arr[right]
        elif sum > n:
            sum -= arr[left]
            left += 1
    return cnt



if __name__ == '__main__':
    arr = [9,5,2,7,0,0,9,0,0,8,7,1,1,2,5,6]
    n = 9
    print(subsum(arr, n))
    print(subsum2(arr, n))