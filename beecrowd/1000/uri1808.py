n = input()
i = 0
qtdzero = s = t = 0
ok = []
okint = []

while i < len(n):
    if len(n) == 1:
        ok.append(n[i])
        break
    elif n[i] != '0':
        ok.append(n[i])
        i = i + 1
    else:
        qtdzero = qtdzero + 1
        i += 1

for j in range(len(ok)):
    okint.append(int(ok[j]))

s = sum(okint)
t = len(okint)

if(qtdzero > 0):
    s -= qtdzero

s += 10 * qtdzero
media = s / t

print('{0:.2f}'.format(media))