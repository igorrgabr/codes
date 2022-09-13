t = 0
while True:
    n = int(input())
    t += 1
    if n == 0:
        break

    x = v = -10000
    y = u = 10000
    for i in range(n):
        l = list(map(int,input().split()))
        if l[0] > x:
            x = l[0]
        if l[1] < y:
            y = l[1]
        if l[2] < u:
            u = l[2]
        if l[3] > v:
            v = l[3]
    
    print(f'Teste {t}')
    if x < u and v < y:
        print(x,y,u,v)
    else:
        print('nenhum')
    print('')