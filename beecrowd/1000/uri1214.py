c = int(input())
for i in range(c):
    n = list(map(int,input().split()))
    media = (sum(n) - n[0]) / n[0]
    qtd = 0
    for k in range(1,len(n)):
        if n[k] > media:
            qtd += 1
    print(f'{((qtd*100)/n[0]):.3f}%')