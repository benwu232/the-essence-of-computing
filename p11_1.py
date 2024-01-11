
s = [7, 1, 4, 3, 5, 5, 9, 4, 10, 25, 11, 12, 33, 2, 13, 6]


def max_subsequence(s):
    lut = {}
    max_cnt = 1
    max_element = -1
    for e in s:
        cnt = lut.get(e-1)
        if cnt is None:
            lut[e] = 1
        else:
            lut[e] = cnt + 1
            lut.pop(e-1)
        if max_cnt < lut[e]:
            max_cnt = lut[e]
            max_element = e
    return max_element, max_cnt, lut

def max_subset1(s):
    _, _, lut = max_subsequence(s)

    max_cnt = 1
    max_element = -1
    dict_modified = True
    while dict_modified:
        dict_modified = False
        for e, cnt in lut.items():
            if max_cnt < cnt:
                max_cnt = cnt
                max_element = e
            cnt2 = lut.get(e-cnt) 
            if cnt2:
                lut[e] += cnt2
                lut.pop(e-cnt)
                dict_modified = True
                break
    return max_element, max_cnt, lut
        
def max_subset2(s):
    _, _, lut = max_subsequence(s)

    max_cnt = 1
    max_element = -1
    dict_modified = True
    idx = 0
    elements = list(lut.keys())
    while idx < len(lut):
        e = elements[idx]
        if lut[e] == -1:
            idx += 1
            continue
        cnt = lut[e]
        if max_cnt < cnt:
            max_cnt = cnt
            max_element = e
        cnt2 = lut.get(e-cnt) 
        if cnt2:
            lut[e] += cnt2
            lut[e-cnt] = -1
            idx -= 1
        idx += 1
    return max_element, max_cnt, lut
 

if __name__ == '__main__':
    max_element, max_cnt, _ = max_subsequence(s)
    print(max_element, max_cnt)

    # max_element, max_cnt, _ = max_subset1(s)
    max_element, max_cnt, _ = max_subset2(s)
    print(max_element, max_cnt)