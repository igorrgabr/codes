tri = list(map(int,input().split()))
ord = sorted(tri)
if ord[0] + ord[1] > ord[2]:
  if ord[2]**2 == ord[0]**2 + ord[1]**2:
    print("r")
  elif ord[2]**2 < ord[0]**2 + ord[1]**2:
    print("a")
  elif ord[2]**2 > ord[0]**2 + ord[1]**2:
    print("o")
else:
  print("n")