def fat(x):
    f = 1
    if x == 0:
        return 1
    for i in range(1,x+1):
        f *= i
    return f
while True:
    try:
        m, n = map(int,input().split())
        print(fat(m)+fat(n))
    except EOFError:
        break