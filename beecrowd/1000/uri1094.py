N = int(input())
total = 0
c = 0
r = 0
s = 0
l = []
ln = []

for i in range(N):
    an = input()
    l.append(an.split()[1])
    aux = an.split()[0]
    total += int(aux)
    ln.append(int(aux))

for i in range(N):
    if l[i] == "C":
        c += ln[i]
    
    elif l[i] == "R":
        r += ln[i]

    elif l[i] == "S":
        s += ln[i]

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {(c*100)/total:.2f} %")
print(f"Percentual de ratos: {(r*100)/total:.2f} %")
print(f"Percentual de sapos: {(s*100)/total:.2f} %")