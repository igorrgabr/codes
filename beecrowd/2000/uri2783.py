m = input().split()
x = list(map(int,input().split()))
y = list(map(int,input().split()))
qtd = 0
for i in x:
    if not i in y:
        qtd += 1
print(qtd)