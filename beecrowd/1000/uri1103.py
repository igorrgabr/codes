while True:
    h1,m1,h2,m2 = map(int,input().split())
    i = 0
    f = 0

    if m1 == m2 == h1 == h2 == 0:
        break

    if h1 == 0:
        i = (24 * 60) + m1
    else:
        i = (h1 * 60) + m1

    if h2 == 0:
        f = (24 * 60) + m2
    else:
        f = (h2 * 60) + m2

    if f > i:
        print(f - i)
    else:
        print((24 * 60) - (i - f))