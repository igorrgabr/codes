L, D = map(int,input().split())
K, P = map(int,input().split())
qtd = L // D
custo = (K * L) + (P * qtd)
print(custo)