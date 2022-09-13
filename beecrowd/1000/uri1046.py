start,end = map(int,input().split())
time = 24
if start > end:
  time = (24 - start) + end
elif end > start:
  time = end - start
print(f"O JOGO DUROU {time} HORA(S)")