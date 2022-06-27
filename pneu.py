N = int(input())
M = int(input())
dif = 0
if N > M:
    dif = N - M
else:
    dif = -(M - N)
print(dif)