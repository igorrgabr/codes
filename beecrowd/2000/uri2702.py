C,B,P = map(int,input().split())
nC,nB,nP = map(int,input().split())
qtd = 0
if C < nC:
  qtd += nC - C
if B < nB:
  qtd += nB - B
if P < nP:
  qtd += nP - P
print(qtd)