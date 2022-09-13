triangle = list(map(int,input().split()))
ord = sorted(triangle)
if ord[0] + ord[1] > ord[3] or ord[0] + ord[2] > ord[3] or ord[1] + ord[2] > ord[3] or ord[0] + ord[1] > ord[2]:
  print("S")
else:
  print("N")