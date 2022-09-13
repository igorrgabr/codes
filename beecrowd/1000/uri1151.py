N = int(input())
f = [0, 1]

while len(f) < N:
    f.append(f[-1] + f[-2])

print(" ".join(map(str,f)))