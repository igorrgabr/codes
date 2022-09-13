n = int(input())
k = int(input())
comp = []
for i in range(n):
    comp.append(int(input()))
comp.sort(reverse=True)
qtd = k
while qtd < n and comp[qtd] == comp[qtd - 1]:
    qtd += 1
print(qtd)