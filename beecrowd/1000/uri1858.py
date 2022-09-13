N = int(input())
num = list(map(int,input().split()))

menor = num[0]
for i in range(N):
    if num[i] < menor:
        menor = num[i]

t = num.index(menor) + 1
print(t)