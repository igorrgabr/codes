while True:
    n, m = map(int,input().split())

    if n == m == 0:
        break

    t = list(map(int,input().split()))
    tnew = list(set(t))
    qtd = 0

    for i in range(len(tnew)):
        if t.count(tnew[i]) >= 2:
            qtd += 1

    print(qtd)