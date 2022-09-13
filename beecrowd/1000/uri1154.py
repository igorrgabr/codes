s = 0
qtd = 0

while True:
    age = int(input())
    if age < 0:
        break
    else:
        s += age
        qtd += 1

print(f"{s/qtd:.2f}")