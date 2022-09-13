P, N = map(int,input().split())

h = list(map(int,input().split()))

count = 0
for i in range(1,len(h)):
    if abs(h[i] - h[i-1]) > P:
        count += 1
        break

if count != 0:
    print("GAME OVER")
else:
    print("YOU WIN")