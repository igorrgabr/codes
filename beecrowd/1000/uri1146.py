while True:
    num = int(input())
    l = []
    if num == 0:
        break
    for i in range(1,num+1):
        l.append(i)
    print(' '.join(map(str, l)))