andar1 = int(input())
andar2 = int(input())
andar3 = int(input())
t1 = 2 * andar2 + 4 * andar3
t2 = 2 * andar1 + 2 * andar3
t3 = 4 * andar1 + 2 * andar2
menort = 0
if t1 <= t2 and t1 <= t3:
  menort = t1
elif t2 <= t3:
  menort = t2
else:
  menort = t3
print(menort)