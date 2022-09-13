t = int(input())
for i in range(t):
    d, n = map(int,input().split())
    p = list(map(float,input().split()))
    c = 0.0
    for j in p:
        if c < (d % j) and (j < d):
            c = d % j
    print(f'{c:.2f}')