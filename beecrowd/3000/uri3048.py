n = int(input())
l = []
qtd = 1
for i in range(n):
    v = int(input())
    l.append(v)
    if l[i] != l[i-1]:
        qtd += 1
print(qtd)