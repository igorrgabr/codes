T = int(input())
A,B,C,D,E = map(int,input().split())
qtd = 0
if A == T:
    qtd += 1
if B == T:
    qtd += 1
if C == T:
    qtd += 1
if D == T:
    qtd += 1
if E == T:
    qtd += 1
print(qtd)