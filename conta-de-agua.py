N = int(input())
price = 0
if N <= 10:
  price = 7
elif N <= 30:
  price = (N - 10) * 1 + 7
elif N <= 100:
  price = (N - 30) * 2 + 7 + 20
elif N > 100:
  price = (N - 100) * 5 + 7 + 20 + 140
print(price)