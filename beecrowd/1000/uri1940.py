j, r = map(int,input().split())
v = list(map(int,input().split()))
p = [0] * j
for i in range(len(v)):
    p[i % j] += v[i]

p.reverse()
for i in range(len(p)):
    if p[i] == sorted(p)[::-1][0]:
        print(len(p) - i)
        break