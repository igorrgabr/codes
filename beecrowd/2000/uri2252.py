def repeat(l):
    rpt = {}
    c = 0
    m = 0
    for i in range(len(v)):
        if v.count(v[i]) > 1:
            c += 1
            rpt[c] = i
            if rpt[c] > m:
                m = rpt[c]
    return m
c = 0
while True:
    try:
        n = int(input())
        v = list(map(float, input().split()))
        vnew = sorted(v, reverse=True)
        password = ''
        c += 1
        for j in range(0, n):
            d = str(v.index(vnew[j]))
            if vnew.count(vnew[j]) > 1:
                d = str(repeat(v))
                vnew = [*set(vnew)]
            password += d
        print(f'Caso {c}: {password}')
    except EOFError:
        break