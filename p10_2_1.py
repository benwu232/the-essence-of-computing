

def cal_combination(n, k):
    product = 1
    for i in range(k):
        product *= n - i
        product //= i + 1
    return product


if __name__ == '__main__':
    r = cal_combination(20, 5) / 2 ** 20
    print(r)
