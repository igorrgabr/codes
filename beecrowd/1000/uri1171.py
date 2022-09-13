N = int(input())
l = {}
for i in range(N):
    num = int(input())
    if num in l:
        l[num] += 1
    else:
        l[num] = 1
k = l.keys()
k = sorted(k)
for i in k:
    print(f'{i} aparece {l[i]} vez(es)')