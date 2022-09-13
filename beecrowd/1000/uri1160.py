t = int(input())
for i in range(t):
    pa,pb,ga,gb = map(float, input().split())
    pa = int(pa)
    pb = int(pb)
    y = 0
    while pa <= pb:
        pa = int(pa*(1 + ga/100))
        pb = int(pb*(1 + gb/100))
        y += 1
        if y > 100:
            print('Mais de 1 seculo.')
            break
    if y <= 100:
        print(f'{y} anos.')