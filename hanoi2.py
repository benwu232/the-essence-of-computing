
cnt = 0

def hanoi(n, src, dst, tmp):
    global cnt
    if n == 1:
        cnt += 1
        print(f'{cnt}: move 1 from {src} to {dst}')
        # move(src, dst)
        return
    hanoi(n-1, src, tmp, dst)
    cnt += 1
    print(f'{cnt}: move {n} from {src} to {dst}')
    hanoi(n-1, tmp, dst, src)

if __name__ == '__main__':
    hanoi(4, 'a', 'b', 't')
