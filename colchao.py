A, B, C = map(int,input().split())
H, L = map(int,input().split())
if A <= H and B <= L:
  print("S")
elif A <= H and C <= L:
  print("S")
elif B <= H and A <= L:
  print("S")
elif B <= H and C <= L:
  print("S")
elif C <= H and A <= L:
  print("S")
elif C <= H and B <= L:
  print("S")
else:
  print("N")