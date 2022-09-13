x, y = map(int,input().split())
if 0 <= y <= 2:
  print("nova")
elif 3 <= y <= 96 and y - x > 0:
  print("crescente")
elif 3 <= y <= 96 and y - x < 0:
  print("minguante")
elif 97 <= y <= 100:
  print("cheia")