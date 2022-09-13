test = 0
while True:
  N = int(input())
  if N > 0:
    tickets = list(map(int,input().split()))
    test += 1
    print(f"Teste {test}")
    for i, pos in enumerate(tickets, 1):
      if i == pos:
        print(i)
    print()
  else:
    break