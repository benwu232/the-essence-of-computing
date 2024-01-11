

def move(src, dst):
    print(f'move from {src} to {dst}')

def hanoi(n, src, dst, tmp):
    if n == 1:
        print(f'move 1 from {src} to {dst}')
        # move(src, dst)
        return
    hanoi(n-1, src, tmp, dst)
    # move(src, dst)
    print(f'move {n} from {src} to {dst}')
    hanoi(n-1, tmp, dst, src)

if __name__ == '__main__':
    hanoi(3, 'a', 'b', 't')
