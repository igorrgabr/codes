A, B, C = map(int,input().split())
X, Y, Z = map(int,input().split())
qtd = 0
if Z >= C:
    qtd = (Z // C) * (X // A) * (Y // B)
print(qtd)